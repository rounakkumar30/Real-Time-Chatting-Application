

```markdown
# 💬 Django Real-Time Chat Application  

## 📌 Project Overview  
A **real-time chat application** built with **Django, WebSockets, and Channels**, allowing users to **send and receive messages instantly**. The app features **secure authentication, private & group chats, and a responsive UI**.  

---

## 🚀 Features  

### 🔹 **Real-Time Messaging**  
- ⚡ Powered by **WebSockets & Django Channels**.  
- 📩 **Instant message delivery** without refreshing the page.  

### 🔐 **User Authentication & Security**  
- ✅ **Email Verification** – Secure user sign-up with email confirmation.  
- 🔑 **Password Reset & Account Management** – Users can change/reset passwords.  

### 🗂 **Chat Features**  
- 👫 **One-on-One Chat** – Users can chat privately.  
- 🌐 **Group Chat** – Create and join group conversations.  
- 🔔 **Notifications** – Get notified of new messages.  

### 🎛 **Admin Panel**  
- 🔧 **Manage users, chat rooms, and messages**.  
- 🔑 **Secure Django admin authentication**.  

---

## ⚙️ Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/rounakkumar30/Real-Time-Chatting-Application.git 
cd django-chat-app
```

### 2️⃣ Create Virtual Environment  

#### ➤ Mac/Linux  
```bash
python3 -m venv venv
source venv/bin/activate
```

#### ➤ Windows  
```bash
python3 -m venv venv
.\venv\Scripts\activate.bat
```

### 3️⃣ Install Dependencies  
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Migrate to Database  
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5️⃣ Run the Application  
```bash
python manage.py runserver
```
Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser.  

### 6️⃣ Generate Secret Key (**Important for Deployment**)  
```bash
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```

---

## 🛠 Tech Stack  
- **Backend:** Django, Django Channels, WebSockets  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** PostgreSQL/SQLite  
- **Authentication:** Django Auth, Email Verification  

---

## 🤝 Contribution  
Feel free to **fork** the repository, create a **feature branch**, and submit a **pull request**!  

📌 **GitHub Repository:** https://github.com/rounakkumar30/Real-Time-Chatting-Application.git

---

## 📩 Contact  
🔹 **Author:** Rounak Kumar  
🔹 **LinkedIn:** https://www.linkedin.com/in/rounakkumar30/ 
🔹 **Email:** rounakverma30march@gmail.com

---

### ⭐ **If you like this project, don't forget to give it a star!** ⭐  
