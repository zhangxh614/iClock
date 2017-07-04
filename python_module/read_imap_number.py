import imaplib
try:
    from mail_account import user_name, pass_wd
except:
    print('account not found')


def get_unseen_number():
    Mail = imaplib.IMAP4_SSL("mails.tsinghua.edu.cn")

    try:
        try:
            Mail.login(user_name, pass_wd)
        except Exception as e:
            print('login error: %s' % e)
            return None
        Mail.select("INBOX")
        tpy, data = Mail.search(None, 'UNSEEN')
        data = data[0].split()
        return len(data)
    except Exception as e:
        print('imap error: %s' % e)
        Mail.close()
        return None
