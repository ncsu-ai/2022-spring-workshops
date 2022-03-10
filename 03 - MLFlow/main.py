import tempfile

import torch
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import mlflow
import click

from net import Net


def load_data(batch_size_train, batch_size_test):
    tmpdir = tempfile.mkdtemp()

    train_loader = torch.utils.data.DataLoader(
        torchvision.datasets.MNIST(
            tmpdir, train=True, download=True,
            transform=torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize(
                    (0.1307,), (0.3081,))
            ])
        ),
        batch_size=batch_size_train, shuffle=True
    )

    test_loader = torch.utils.data.DataLoader(
        torchvision.datasets.MNIST(
            tmpdir, train=False, download=True,
            transform=torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize(
                    (0.1307,), (0.3081,))
            ])
        ),
        batch_size=batch_size_test, shuffle=True
    )

    mlflow.log_artifacts(f'{tmpdir}/MNIST', 'mnist_data')
    return train_loader, test_loader


def train(network, optimizer, train_loader, epoch, log_interval):
    tmpdir = tempfile.mkdtemp()

    network.train()
    for batch, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = network(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()

        if batch % log_interval == 0:
            mlflow.log_metric(f'Training Loss - Epoch {epoch}', loss.item(), batch * len(data))

            n_complete = batch * len(data)
            n_total = len(train_loader.dataset)
            pct_complete = 100. * batch / len(train_loader)
            print(f'Train Epoch: {epoch} [{n_complete}/{n_total} ({pct_complete:.0f}%)]\tLoss: {loss.item():.6f}')

            torch.save(network.state_dict(), f'{tmpdir}/model.pth')
            torch.save(optimizer.state_dict(), f'{tmpdir}/optimizer.pth')

    mlflow.log_artifacts(tmpdir, 'model_state')


def test(network, test_loader, epoch):
    network.eval()
    test_loss = 0
    correct = 0

    with torch.no_grad():
        for data, target in test_loader:
            output = network(data)
            test_loss += F.nll_loss(output, target, size_average=False).item()
            pred = output.data.max(1, keepdim=True)[1]
            correct += pred.eq(target.data.view_as(pred)).sum()

    n_total = len(test_loader.dataset)
    test_loss /= n_total
    pct_correct = 100. * correct / n_total

    mlflow.log_metric('Test Accuracy', pct_correct.item(), epoch)
    mlflow.log_metric('Average Test Loss', test_loss, epoch)
    print(f'\nTest set: Avg. loss: {test_loss:.4f}, Accuracy: {correct}/{n_total} ({pct_correct:.0f}%)\n')


@click.command('Trains a neural network to classify images from the MNIST data set')
@click.option('--batch_size_train', default=64)
@click.option('--batch_size_test', default=10000)
@click.option('--n_epochs', default=3)
@click.option('--learning_rate', default=0.01)
@click.option('--momentum', default=0.5)
@click.option('--log_interval', default=10)
@click.option('--random_seed', default=1)
def train_network(batch_size_train, batch_size_test, n_epochs, learning_rate, momentum, log_interval, random_seed):
    with mlflow.start_run():
        train_loader, test_loader = load_data(batch_size_train, batch_size_test)

        torch.backends.cudnn.enabled = False
        torch.manual_seed(random_seed)

        network = Net()
        optimizer = optim.SGD(network.parameters(), lr=learning_rate, momentum=momentum)

        test(network, test_loader, 0)
        for epoch in range(1, n_epochs + 1):
            train(network, optimizer, train_loader, epoch, log_interval)
            test(network, test_loader, epoch)


if __name__ == '__main__':
    train_network()
