"""Create a thing in AWS IoT"""

THING_NAME = "myThingName"
POLICY_NAME = 'PubSubToAnyTopic'
POLICY = 'file://iotpolicy.json'
#ARN = "YOUR AWS IOT ENDPOINT"

def run_command(cmd):
    """Execute command"""

    from subprocess import Popen, PIPE
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    (out, err) = p.communicate()
    print 'Return code: ', p.returncode, err, out
    return out

def main(args=None):
    """main function"""


    rst = run_command(['aws', 'iot', 'describe-endpoint'])
    import json
    ARN = json.loads(rst)['endpointAddress']
	
    run_command(['aws', 'iot', 'create-thing', '--thing-name', THING_NAME])
    run_command(['aws', 'iot', 'create-keys-and-certificate', '--set-as-active', '--certificate-pem-outfile', 'cert.pem', '--public-key-outfile', 'publicKey.pem'])
    run_command(['aws', 'iot', 'create-policy', '--policy-name', POLICY_NAME, '--policy-document', POLICY ])
    run_command(['aws', 'iot', 'attach-principal-policy', '--principal', ARN, '--policy-name', POLICY_NAME])
    run_command(['aws', 'iot', 'attach-thing-principal', '--thing-name', THING_NAME, '--principal', ARN])
    run_command(['aws', 'iot', 'list-things'])
if __name__ == "__main__":
    main()

