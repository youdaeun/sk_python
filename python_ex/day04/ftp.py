import ftplib

hostname = "hostname"
ftp = ftplib.FTP(hostname)
ftp.login('msfadmin','msfadmin')
ftp.retrlines('LIST')

with open("1_result.xlsx","rb") as file:
    ftp.storbinary(f"STOR 1_result.xlsx",file)

print(f"현재 작업 디렉터리 : {ftp.pwd()}")
ftp.retrlines('LIST')

ftp.quit()
