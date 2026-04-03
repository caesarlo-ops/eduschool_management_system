# Quick Railway Deployment Checklist

## 🚀 Pre-Deployment (On Your Computer)

### 1. Install Git
- [ ] Download from https://git-scm.com/downloads
- [ ] Install and restart computer if needed
- [ ] Verify: `git --version` in PowerShell

### 2. Initialize Git Repository
```powershell
cd "c:\Users\USER\OneDrive\Desktop\School Manangement\school_management"
git init
```
- [ ] Git repository initialized

### 3. Add All Files
```powershell
git add .
```
- [ ] All files staged

### 4. Commit Changes
```powershell
git commit -m "Railway deployment ready"
```
- [ ] Changes committed

### 5. Create GitHub Account
- [ ] Go to https://github.com
- [ ] Sign up/Login
- [ ] Create new repository named `school-management`
- [ ] Copy the repository URL

### 6. Push to GitHub
```powershell
git remote add origin https://github.com/YOUR_USERNAME/school-management.git
git branch -M main
git push -u origin main
```
- [ ] Code pushed to GitHub

---

## 🚀 Railway Setup (Online)

### 7. Create Railway Account
- [ ] Go to https://railway.app
- [ ] Sign up with GitHub account

### 8. Deploy from GitHub
- [ ] Click "New Project"
- [ ] Select "Deploy from GitHub repo"
- [ ] Choose `school-management` repository
- [ ] Click "Deploy Now"
- [ ] Wait for build to complete

### 9. Add PostgreSQL Database
- [ ] In Railway dashboard, click "+ New"
- [ ] Select "Database" → "PostgreSQL"
- [ ] Wait for database to provision
- [ ] Railway auto-connects it to your app!

### 10. Set Environment Variables
In Railway dashboard → Your Service → Variables:

| Variable | Value |
|----------|-------|
| SECRET_KEY | `-rv^+)j8_dl$u)o71zslaygb+pghvlxqih5gcxp706n=xrmu1f` |
| DEBUG | `False` |
| ALLOWED_HOSTS | `kdfinancesolutions.co.zw,www.kdfinancesolutions.co.zw,185.150.189.233,your-railway-url.railway.app` |

- [ ] SECRET_KEY added
- [ ] DEBUG set to False
- [ ] ALLOWED_HOSTS configured

---

## 🗄️ Database Setup (In Railway Shell)

### 11. Open Railway Shell
- [ ] Click on your service in Railway
- [ ] Go to "Shell" tab
- [ ] Wait for shell to open

### 12. Run Migrations
```bash
python manage.py migrate
```
- [ ] All migrations applied successfully

### 13. Create Admin User
```bash
python manage.py createsuperuser
```
- [ ] Username entered
- [ ] Email entered
- [ ] Password entered (twice)
- [ ] Superuser created

### 14. Collect Static Files
```bash
python manage.py collectstatic --noinput
```
- [ ] Static files collected

---

## 🌐 Testing & Domain

### 15. Test Your App
- [ ] Copy Railway URL from dashboard
- [ ] Visit in browser
- [ ] Login page loads
- [ ] CSS/styles working
- [ ] Can login with admin account

### 16. Connect Custom Domain (Optional)
**In Railway:**
- [ ] Settings → Networking
- [ ] Add Custom Domain: `kdfinancesolutions.co.zw`

**At domain provider:**
- [ ] Add CNAME record pointing to Railway URL
- [ ] OR Add A record with Railway's IP
- [ ] Wait 24-48 hours for DNS propagation

---

## ✅ Final Checks

- [ ] Application is live and accessible
- [ ] Admin panel works (`/admin/`)
- [ ] Database is connected
- [ ] Static files (CSS) loading properly
- [ ] No errors in Railway logs
- [ ] Custom domain working (if applicable)

---

## 🎉 Congratulations!

Your School Management System is now live on Railway! 🚀

**Access it at:**
- Railway URL: `https://your-project.up.railway.app`
- Custom domain: `http://kdfinancesolutions.co.zw` (after DNS)

---

## 📞 Quick Reference

**Railway Dashboard:** https://railway.app  
**Railway Docs:** https://docs.railway.app  
**GitHub Repo:** https://github.com/YOUR_USERNAME/school-management  

**Admin Panel:** `https://your-url.railway.app/admin/`  
**Login Page:** `https://your-url.railway.app/login/`

---

## 🔧 Common Issues & Fixes

| Problem | Solution |
|---------|----------|
| Build fails | Check Procfile exists |
| App won't start | Check environment variables |
| Database error | Ensure PostgreSQL is added |
| CSS not loading | Run collectstatic again |
| Allowed Hosts error | Add Railway URL to ALLOWED_HOSTS |

---

**Last Updated:** Thursday, March 26, 2026
