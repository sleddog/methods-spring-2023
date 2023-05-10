
# PackPoint

PackPoint is a location sharing app where people can add their favorite spots to a public map whether it is a cool hike, good food, or good study spot. Download it now on the [App Store](https://apps.apple.com/us/app/packpoint/id6448881272)!
## Screenshots

![App Screenshots](https://i.imgur.com/0crQVJO.png)
## Documentation

PackPoint is made up of a client side iOS App, and a backend server hosted on Azure. You can find more details about each below.

### Client Side (iOS App)

The iOS app was made with Xcode. It uses mostly SwiftUI with some UIKit Elements. The app follows the MVVC or Model-View-ViewModel Pattern. Most of the logic is done in the backend but there are some things that are needed to be done on the client side such as authentification and some formatting for data before sending it to the API. The authentification is handled by firebase phone authentification. The app sends a request to firebase with a users phone number. The app then verifies the user is real by either sending an APN (silent push notification) or a reCaptcha to the user. Once that is successful, Firebase then sends a text to the user with a 6 digit code. The user enters this code on the verification code page, if the code is correct, the user is logged in/signed up. This was my first serious app I have ever made. It was a bit of a process and it wasnt perfect, but I am pretty happy as I only spent ~2 weeks on it on and off with school. 

### Server Side (Azure Hosted Backend)

The server side is where most of the logic happens. The tech stack for this involves the following:

- Typescript
- Node.js
- Express.js
- PostgreSQL DB
- Azure Blob Storage
- Azure App Service
- Firebase Admin

The backend for this app has two main tables, a user table and a points table. The user table pretty much just stores the users phone number and their Firebase UID. The points table stores a lot more including all the basic info for the point (name, description, rating, etc), as well as the blob link to the image, and the users Firebase UID which is liked as a foreign key to the user table. The controllers are also split up into user controllers and point controllers. The client app can then call most of these endpoints to complete tasks like get nearby points. As mentioned, the app is hosted as an Azure App Service. This makes it so that I dont need to have my computer running all the time, instead Azure handles that for me. This wasnt my first time working with most of these technologies, but it was my second time lol. I am still very new to all of this but was pretty happy with what I was able to come up with in a limited time.


## Acknowledgements

The design and idea for this app was made by me and my group members at DubHacks 22'. My group members were Gillian Soekawan, Nathan Sidik, and Pim Jit. DubHacks 22' is a hackathon hosted by the University of Washington. The hackathon was only 24 hours long so we werent able to get super far, but we still finished as finalists. It was a very fun and a great experience with a great team. I was happy to finally be able to bring this app to life for this project.


## More Info

Below you will find links to our devpost submission and server repo. You may need to request access if you want to look at the repos because they have some private data that I havent cleared out yet.

[Devpost](https://devpost.com/software/packpoint)

[Packpoint Repo](https://github.com/Skeegan123/packpoint2)

[Packpoint Server Repo](https://github.com/Skeegan123/packpoint2-backend)

