import ftplib
import os

# Compile the latest unit tests
os.system("./gradlew test")
# Compile latest code coverage report
os.system("./gradlew jacocoTestReport")
# Compile latest java docs
os.system("./gradlew javadoc")

# Upload unit tests via FTP to server
print("Starting to deploy latest unit test report to docs.ekbjarnason.com")
ftp = ftplib.FTP('cptropaeolum.arvixe.com')
ftp.login('tictactoe', 'ticTacTo3')
ftp.cwd('docs.ekbjarnason.com/wwwroot/junit')
for root, dirs, files in os.walk('build/reports/tests'):
	for fname in files:
		full_fname = os.path.join(root, fname)
		correctPath = full_fname.split("tests")[1]
		correctPath = correctPath[1:].replace("\\", "/")
		ftp.storbinary('STOR ' + correctPath, open(full_fname, 'rb'))
print("Unit test deployment report completed")

# Upload Code coverage report via FTP to server
print("Starting to deploy latest code coverage test report to docs.ekbjarnason.com")
ftp.cwd('../jacoco')
for root, dirs, files in os.walk('build/reports/jacoco/test/html'):
	for fname in files:
		full_fname = os.path.join(root, fname)
		correctPath = full_fname.split("html", 1)[1][1:]
		ftp.storbinary('STOR ' + correctPath, open(full_fname, 'rb'))
print("Code coverage test report deployment completed")

# Compile latest Selenium tests
os.system("./gradlew selenium")

# Upload selenium test report via FTP to server
print("Starting to deploy latest selenium test report to docs.ekbjarnason.com")
ftp.cwd('../selenium')
for root, dirs, files in os.walk('build/reports/tests'):
	for fname in files:
		full_fname = os.path.join(root, fname)
		correctPath = full_fname.split("tests")[1]
		correctPath = correctPath[1:].replace("\\", "/")
		ftp.storbinary('STOR ' + correctPath, open(full_fname, 'rb'))
print("Selenium test report deployment completed")

# Upload java docs via FTP to server
print("Starting to deploy latest java docs to docs.ekbjarnason.com")
ftp.cwd('../javadoc')
for root, dirs, files in os.walk('build/docs/javadoc'):
	for fname in files:
		full_fname = os.path.join(root, fname)
		full_fname = full_fname.replace("\\", "/")
		correctPath = full_fname.split("javadoc")[1]
		correctPath = correctPath[1:]
		ftp.storbinary('STOR ' + correctPath, open(full_fname, 'rb'))
print("Java docs deployment completed")

# Close the FTP stream
ftp.quit()
