# Notifier
A python tool that monitor system services and send notification about the status of the services.

### 1. Run example Node.js service in terminal.

```bash
$ node app.js
```

### 2. Now run Notifier along side in another terminal and stop the node service to see the notification.

```bash
$ python3 notifier.py
```

### 3. To see dashboard and add your configurations via form.
 #### Navigate to *django* folder and run below command

  ```bash
  $ python3 manage.py runserver
  ```
  Access *http://127.0.0.1:8000/*

#### You can also add your services and twilio configurations in config.json manually.

## Screenshots

Initializing node server and notifier in two termninals

<img width="619" alt="Screenshot 2022-06-19 at 2 55 33 PM" src="https://user-images.githubusercontent.com/46554685/174474365-d6350efa-2914-474a-b72e-bf612dda94bf.png">

Stopped server due to unhandled error event occured

<img width="790" alt="Screenshot 2022-04-10 at 7 17 28 PM" src="https://user-images.githubusercontent.com/46554685/174474397-42f0b518-db4c-4091-9ef8-eac1d41af238.png">

Server restarted and notifications sent

<img width="925" alt="Screenshot 2022-06-19 at 2 58 20 PM" src="https://user-images.githubusercontent.com/46554685/174474501-748b4d9f-2e3d-4fb3-b6cb-1e4f7a1dc84e.png">

Django dashboard with various system information

<img width="1440" alt="Screenshot 2022-06-19 at 3 19 31 PM" src="https://user-images.githubusercontent.com/46554685/174475321-071af3fd-ab7b-42b6-be25-2ee542acf563.png">

Django form to add your configs

<img width="1440" alt="Screenshot 2022-06-19 at 3 01 08 PM" src="https://user-images.githubusercontent.com/46554685/174474609-bd1e1673-a333-4e07-953c-6daee35283e1.png">
