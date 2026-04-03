# 🚀 Quick Start - Railway Deployment

## Your School Management System is Now Railway-Ready! ✨

---

## ⚡ Super Quick Deployment (3 Steps)

### **Step 1:** Run the Setup Script

Open PowerShell in this folder and run:

```powershell
.\setup-railway.ps1
```

This will prepare your project for Railway.

---

### **Step 2:** Push to GitHub

1. Go to https://github.com and create a new repository named `school-management`
2. Copy the repository URL
3. In PowerShell, run:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/school-management.git
git branch -M main
git push -u origin main
```

---

### **Step 3:** Deploy on Railway

1. Go to https://railway.app
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your `school-management` repository
5. Click **"Deploy Now"**
6. Add a **PostgreSQL** database (+ New → Database → PostgreSQL)
7. Set environment variables (see below)

---

## 🔧 Environment Variables for Railway

In Railway dashboard → Your Service → Variables, add:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | `-rv^+)j8_dl$u)o71zslaygb+pghvlxqih5gcxp706n=xrmu1f` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `kdfinancesolutions.co.zw,www.kdfinancesolutions.co.zw,185.150.189.233,your-railway-url.railway.app` |

---

## 🗄️ Database Setup (After Deployment)

1. Click on your service in Railway
2. Go to **"Shell"** tab
3. Run these commands:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

---

## 🎉 Done!

Your app is now live at: `https://your-project.up.railway.app`

---

## 📁 What Was Configured

✅ **settings.py** - Made environment-variable friendly  
✅ **requirements.txt** - Added Gunicorn & WhiteNoise  
✅ **Procfile** - Tells Railway how to run your app  
✅ **railway.json** - Railway configuration  
✅ **.gitignore** - Prevents uploading unnecessary files  

---

## 📖 Need More Help?

- **Detailed Guide:** See `RAILWAY_DEPLOYMENT.md`
- **Checklist:** See `DEPLOYMENT_CHECKLIST.md`
- **Railway Docs:** https://docs.railway.app

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Build fails | Make sure Procfile exists |
| App won't start | Check environment variables |
| Database error | Add PostgreSQL in Railway dashboard |
| CSS not loading | Run `collectstatic` in Railway shell |

---

**Good luck with your deployment!** 🚀✨
