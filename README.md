# Instagram Replica   

## Introduction  
This project focuses on building an Instagram Clone application using Python Flask and Google Cloud services. The app allows users to register, log in, create posts, edit their profiles, and interact with posts through comments and browsing. It replicates essential social media functionalities, providing a simplified yet effective platform.  

## Project Outline  
1. **Core Features**:  
   - User registration and login with secure authentication.  
   - Create, edit, and delete posts.  
   - View and comment on posts.  
   - Edit user profiles and upload profile pictures.  

2. **Technologies Used**:  
   - **Flask**: For building the web application framework.  
   - **Google Cloud Storage**: To store user-uploaded images securely.  
   - **Google Datastore**: To manage user information, posts, and comments.  
   - **Flask-WTF**: For handling form submissions.  
   - **Flask-Session**: For managing user sessions.  

3. **Data Models**:  
   - **User**: Stores user details like email, password, profile image, and bio.  
   - **Post**: Tracks post content, images, and associated user details.  
   - **Comment**: Records comments made on posts.  

4. **Utilities**:  
   - Functions for validating user input.  
   - Uploading images to Google Cloud Storage.  
   - Managing relationships between users, posts, and comments.  

## Conclusion  
The Instagram Clone project demonstrates how to build a functional social media application using Flask and Google Cloud. It integrates user-friendly features, secure data handling, and cloud storage for scalability. This project highlights the potential of combining Flask and cloud technologies to develop modern web applications.
