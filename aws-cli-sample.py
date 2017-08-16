"""Create a thing in AWS IoT"""


POLICY = 'file://iotpolicy.json'
import json

with open('config.json') as json_data:
    content = json.load(json_data)
    THING_NAME = content['THING_NAME']
    POLICY_NAME = content['POLICY_NAME']



def run_command(cmd):
    """Execute command"""

    from subprocess import Popen, PIPE
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    (out, err) = p.communicate()
    print 'Return code: ', p.returncode, err, out
    return out

def main(args=None):
    """main function"""
    run_command(['aws', 'iot', 'create-thing', '--thing-name', THING_NAME])
    run_command(['aws', 'iot', 'create-policy', '--policy-name', POLICY_NAME, '--policy-document', POLICY ])
    rst = run_command(['aws', 'iot', 'create-keys-and-certificate', '--set-as-active', '--certificate-pem-outfile', 'cert.pem', '--private-key-outfile', 'privateKey.pem'])
    ARN = json.loads(rst)['certificateArn']

    run_command(['aws', 'iot', 'attach-principal-policy', '--principal', ARN, '--policy-name', POLICY_NAME])
    run_command(['aws', 'iot', 'attach-thing-principal', '--thing-name', THING_NAME, '--principal', ARN])
    run_command(['aws', 'iot', 'list-things'])
if __name__ == "__main__":
    main()

