# method 1 (whatsapp)
# import pywhatkit as pwk
# pwk.sendwhatmsg_instantly("+995555344020","Errors",10,True)

# method 2 (slack)
import requests
import sys
import getopt

slack_key = 'https://hooks.slack.com/services/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'

def send_slack_message(message):
    payload = '{"text":"%s"}' % message
    response = requests.post(slack_key,data=payload)

def main(argv):
    message = ''

    try: opts, args = getopt.getopt(argv,"hm:",["message="])

    except getopt.GetoptError:
        print('sms.py -m <message>')
        sys.exit(2)

    if len(opts) == 0:
        message = "errors"
    for opt ,arg in opts:
        if opt == '-h':
            print('sms.py -m <message>')
            sys.exit()
        elif opt in ("-m","--message"):
            message = arg
    send_slack_message(message)

if __name__ == "__main__":
    main(sys.argv[1:])