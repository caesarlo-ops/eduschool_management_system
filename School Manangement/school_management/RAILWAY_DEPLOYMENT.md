# 🚀 Railway Deployment Guide for School Management System

## Domain: kdfinancesolutions.co.zw

---

## 📋 What I've Configured For You

I've set up your Django project to work perfectly with Railway. Here's what was added:

### ✅ Files Created:
1. **`Procfile`** - Tells Railway how to run your app
2. **`railway.json`** - Railway configuration file
3. **`.gitignore`** - Prevents uploading unnecessary files
4. **`settings_railway.py`** - Alternative Railway settings (backup)

### ✅ Updated Files:
1. **`requirements.txt`** - Added Gunicorn and WhiteNoise
2. **`settings.py`** - Made environment-variable friendly

---

## 🎯 Step-by-Step Deployment Instructions

### **Step 1: Install Git** (if not already installed)

Download and install Git from: https://git-scm.com/downloads

After installation, open PowerShell and verify:
```powershell
PS C:\Users\USER\OneDrive\Desktop\School Manangement> git --version
```

You should see something like: `git version 2.x.x`

---

### **Step 2: Initialize Git Repository**

Open PowerShell in your project folder and run:

```powershell
PS C:\Users\USER\OneDrive\Desktop\School Manangement\school_management> git init
```

**Expected output:** 
```
Initialized empty Git repository in ...
```

---

### **Step 3: Create .gitignore File**

✅ Already done! The `.gitignore` file is created.

---

### **Step 4: Make Your First Commit**

Run these commands one by one:

```powershell
PS C:\Users\USER\OneDrive\Desktop\School Manangement\school_management> git add .
```

```powershell
PS C:\Users\USER\OneDrive\Desktop\School Manangement\school_management> git commit -m "Initial commit - Railway ready"
```

**Expected output:** 
```
[master (root-commit) abc123] Initial commit - Railway ready
 X files changed, X insertions(+)
```

---

### **Step 5: Connect to Railway**

#### Option A: Deploy via GitHub (Recommended)

1. **Push to GitHub first:**
   - Go to https://github.com and create a new repository (name it `school-management`)
   - In PowerShell, run:
   
   ```powershell
   PS C:\Users\USER\OneDrive\Desktop\School Manangement\school_management> git remote add origin https://github.com/YOUR_USERNAME/school-management.git
   ```
   
   ```powershell
   PS C:\Users\USER\OneDrive\Desktop\School Manangement\school_management> git branch -M main
   ```
   
   ```powershell
   PS C:\Users\USER\OneDrive\Desktop\School Manangement\school_management> git push -u origin main
   ```

2. **Deploy on Railway:**
   - Go to https://railway.app
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `school-management` repository
   - Click "Deploy Now"

#### Option B: Deploy via Railway CLI

1. **Install Railway CLI:**
   ```powershell
   npm install -g @railway/cli
   ```

2. **Login to Railway:**
   ```powershell
   railway login
   ```

3. **Initialize Railway project:**
   ```powershell
   railway init
   ```

4. **Deploy:**
   ```powershell
   railway up
   ```

---

### **Step 6: Add PostgreSQL Database**

Railway makes this super easy!

1. In your Railway project dashboard:
   - Click "+ New"
   - Select "Database"
   - Choose "PostgreSQL"
   - Click "Add"

2. Railway will automatically connect the database to your app!

**What happens:** Railway automatically sets these environment variables:
- `PGHOST` - Database host
- `PGPORT` - Database port  
- `PGDATABASE` - Database name
- `PGUSER` - Database username
- `PGPASSWORD` - Database password

Your `settings.py` is already configured to use these! ✨

---

### **Step 7: Configure Environment Variables**

In Railway dashboard, go to your project → Variables tab.

Add these variables:

| Variable Name | Value |
|--------------|-------|
| `SECRET_KEY` | `-rv^+)j8_dl$u)o71zslaygb+pghvlxqih5gcxp706n=xrmu1f` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `kdfinancesolutions.co.zw,www.kdfinancesolutions.co.zw,185.150.189.233,your-railway-url.railway.app` |

**How to find your Railway URL:**
- After deployment, Railway gives you a URL like: `https://your-project-production.up.railway.app`
- Add this to ALLOWED_HOSTS

---

### **Step 8: Run Migrations**

In Railway dashboard:

1. Go to your PostgreSQL service
2. Click on "Connect" → "Copy Connection String"
3. Open Railway Shell (click on your service → Shell tab)
4. Run:

```bash
python manage.py migrate
```

**Expected output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, core, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
```

---

### **Step 9: Create Superuser (Admin Account)**

In the Railway Shell, run:

```bash
python manage.py createsuperuser
```

It will ask you:
- Username: (choose a username)
- Email: (enter your email)
- Password: (enter a strong password)
- Password (again): (confirm password)

**Success message:** `Superuser created successfully`

---

### **Step 10: Collect Static Files**

In Railway Shell, run:

```bash
python manage.py collectstatic --noinput
```

**Expected output:**
```
Found X static file(s)...
Copying ...
X static file(s) copied
```

---

## 🌐 Connecting Your Custom Domain

To use `kdfinancesolutions.co.zw`:

1. **In Railway Dashboard:**
   - Go to Settings → Networking
   - Click "Add Custom Domain"
   - Enter: `kdfinancesolutions.co.zw`

2. **At your domain provider (where you bought the domain):**
   - Add a CNAME record:
     - **Name/Host:** `www` or `@`
     - **Value/Target:** `your-railway-url.up.railway.app`
   
   OR
   
   - Add an A record:
     - **Name/Host:** `@`
     - **Value/Target:** Railway's IP address (they'll provide this)

3. **Wait for DNS propagation** (can take 24-48 hours)

---

## ✅ Testing Your Deployment

After deployment, visit:
- `https://your-railway-url.railway.app`
- `http://kdfinancesolutions.co.zw` (after DNS propagation)

Test these features:
1. ✅ Login page loads
2. ✅ Static files (CSS) working
3. ✅ Admin panel accessible at `/admin/`
4. ✅ Database connections working

---

## 🔧 Troubleshooting

### Problem: "Application failed to launch"
**Solution:** Check your Procfile exists and has correct content:
```
web: gunicorn config.wsgi:application --log-file -
```

### Problem: "Static files not loading"
**Solution:** 
1. Verify WhiteNoise is in requirements.txt
2. Run `python manage.py collectstatic --noinput` again
3. Check MIDDLEWARE has WhiteNoise

### Problem: "Database connection error"
**Solution:**
1. Make sure PostgreSQL is added in Railway
2. Check environment variables are set correctly
3. Restart your Railway service

### Problem: "ALLOWED_HOSTS error"
**Solution:**
Add your Railway URL to ALLOWED_HOSTS environment variable

---

## 📊 Monitoring Your App

View logs in Railway:
- Go to your project → Deployments tab
- Click on latest deployment
- View real-time logs

---

## 💰 Railway Pricing

Railway offers:
- **Free tier:** $5 credit/month (great for testing!)
- **Paid plans:** Starting at $5/month

Your school management system should run fine on the free tier initially.

---

## 🎉 Success Checklist

- [ ] Git repository initialized
- [ ] Code committed to GitHub
- [ ] Railway project created
- [ ] PostgreSQL database added
- [ ] Environment variables configured
- [ ] Migrations ran successfully
- [ ] Superuser created
- [ ] Static files collected
- [ ] App is accessible online
- [ ] Custom domain connected (optional)

---

## 🆘 Need Help?

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Railway Support: support@railway.app

---

Good luck with your deployment! 🚀✨
