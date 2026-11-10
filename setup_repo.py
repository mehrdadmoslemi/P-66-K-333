import os
import subprocess
import sys

def run_command(command):
    """Run a command and return its output and success status."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip(), True
    except subprocess.CalledProcessError as e:
        print(f"Error executing: {command}")
        print(e.stderr)
        return e.stderr, False

def main():
    print("--- شروع عملیات آماده‌سازی مخزن ---")

    # 1. Git Init
    print("[1/4] اجرای git init... ")
    run_command("git init")

    # 2. Add and Commit
    print("[2/4] افزودن و ثبت فایل‌ها (Add & Commit)... ")
    run_command("git add .")
    run_command("git commit -m 'Initial commit: Setup P-66 project structure'")

    # 3. Check for gh CLI and handle remote
    print("[3/4] بررسی وجود gh CLI و تنظیم مخزن راه دور... ")
    gh_exists = subprocess.run("which gh", shell=True).returncode == 0

    if gh_exists:
        print("gh CLI یافت شد. تلاش برای ایجاد مخزن در GitHub...")
        # Try to create a repo using gh. If it already exists or fails, it will fall back to manual instructions.
        # We use a default name but the user can change it if needed.
        create_cmd = "gh repo create P-66-K-333 --public --source . --remote origin --push"
        result, success = run_command(create_cmd)
        
        if success:
            print(f"مخزن با موفقیت ایجاد شد: {result}")
            print(f"URL مخزن: {result}")
        else:
            print("خطا در ایجاد خودکار با gh CLI. احتمالاً مخزن از قبل وجود دارد یا نام تکراری است.")
            print("لطفاً دستورات زیر را به صورت دستی اجرا کنید:")
            print("git remote add origin <URL_مخزن_شما>")
            print("git push -u origin main")
    else:
        print("gh CLI یافت نشد. دستورات زیر را برای اتصال به مخزن دستی کپی و اجرا کنید:")
        print("---------------------------------------------------")
        print("git remote add origin <URL_مخزن_شما>")
        print("git branch -M main")
        print("git push -u origin main")
        print("---------------------------------------------------")

    print("--- عملیات با موفقیت به پایان رسید ---")

if __name__ == "__main__":
    main()