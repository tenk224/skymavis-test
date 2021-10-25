import sys
import random

def random_az(region):
    t = random.randint(0, 2)
    if t == 0:
        return region + '-a'
    elif t == 1:
        return region + '-b'
    else:
        return region + '-c'
    return

def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    nat = []
    subnet = []
    REGION = 'us-west1'

    f = open("problem.txt", "w")
    content = ''

    content += 'NATInstances:\n'
    for i in range(m):
        nat.append(random_az(REGION))
    nat.sort()
    for i in range(m):
        content += '  ' + str(i+1) + ' - ' + nat[i] + '\n'

    content += '\nSubnets:\n'
    for i in range(n):
        subnet.append(random_az(REGION))
    subnet.sort()
    for i in range(n):
        content += '  ' + str(i+1) + ' - ' + subnet[i] + '\n'

    f.write(content)
    f.close()

main()
