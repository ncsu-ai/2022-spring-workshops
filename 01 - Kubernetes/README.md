# Spring 2022 Workshop 01 - Kubernetes

A starter repository for AI Club at NC State's first workshop of the Spring 2022 semester which covers Kubernetes.

### Reference
- [What exactly is Kubernetes?](https://towardsdatascience.com/what-exactly-is-kubernetes-52c9f1c4990b)
- [Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [Get started with Kubernetes (using Python)](https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/)

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
5. TODO: Create venv
6. TODO: Activate venv
7. TODO: Install dependencies
8. TODO: Run Jupyter Notebook
9. Follow along in `Kubernetes.ipynb`





9. Create deployment
10. List your deployments
11. View your deployed app
12. In order for your deployment to be accessible without using the Proxy, you must configure a Service
13. Explore your app
14. View the container logs
15. Executing commands in a container
16. Exposing your app publicly
17. Using labels
18. Deleting a service (need to delete deployment separately)
19. Scale up your app
20. Load balancing
21. Scale down your app
22. Updating your app
23. Verifying your update
24. Rollback your update