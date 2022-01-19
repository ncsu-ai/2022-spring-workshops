# Spring 2022 Workshop 01 - Kubernetes

A starter repository for AI Club at NC State's first workshop of the Spring 2022 semester which covers Kubernetes.

### Prerequisites
1. Install [Docker Desktop](https://www.docker.com/get-started) which comes pre-packaged with a local Kubernetes environment
2. Install [Python 3.7+](https://www.python.org/downloads/) (the workshop was created using Python 3.10, so you may experience compatibility/versioning issues with older versions of Python)

### Workshop Steps
1. Open Docker Desktop and navigate to the Kubernetes settings window.
   1. Click the settings button in the top-right of the Docker Desktop window
   2. Click "Kubernetes" on the left side of the settings window
2. If Kubernetes is not already enabled within Docker Desktop, check the box next to "Enable Kubernetes," then "Apply & Restart" to set up a local Kubernetes server
3. Verify that the Kubernetes command-line tool, `kubectl`, is installed and configured by running the following in your terminal/command prompt:
    ```
    kubectl version
    ```
   Upon running the command, a client and server version should be displayed. If a server version is not shown, additional troubleshooting may be required.
4. Ensure Kubernetes is using the Docker Desktop context:
   ```
   kubectl config use-context docker-desktop
   ```
5. [Create and activate a new virtual environment](https://python.land/virtual-environments/virtualenv)
6. Install Python dependencies
   ```
   pip install -r requirements.txt
   ```
7. Start a Jupyter Notebook server
   ```
   jupyter notebook
   ```
8. Follow along in `01 - Kubernetes/Kubernetes.ipynb`

### Reference
- [What exactly is Kubernetes?](https://towardsdatascience.com/what-exactly-is-kubernetes-52c9f1c4990b)
- [Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [Get started with Kubernetes (using Python)](https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/)
