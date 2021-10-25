def get_zone(t):
    for i in range(len(t)):
        if t[i] == '-':
            return t[i+2:]

def find_min(t,n):
    result = [1000, 0]
    if n == 1:
        return 1
    else:
        i = 1
        while i < len(t):
            j = 1
            sum = 0
            while j < n:
                sum += int(t[i][j])
                j += 1
            if sum < result[0]:
                result[0] = sum
                result[1] = i
            i += 1
        return result[1]

def find_nat_same_zone(nat,zone):
    result = []
    for i in range(len(nat)):
        if zone in nat[i]:
            result.append(i+1)
    return result

def find_min_same_zone(t,nat_index,n):
    result = [1000, 0]
    if n == 1:
        return 1
    else:
        i = 0
        while i < len(nat_index):
            j = 1
            sum = 0
            while j < n:
                sum = sum + int(t[nat_index[i]][j])
                j += 1
            if sum < result[0]:
                result[0] = sum
                result[1] = nat_index[i]
            i += 1
        return result[1]

def main():
    PROBLEM = 'problem.txt'
    nat = []
    sub = []
    t = []

    with open(PROBLEM) as f:
        data = f.readlines()
    i = 0
    while i < len(data):
        if "NATInstances" in data[i]:
            j = i + 1
            while data[j] != '\n':
                nat.append(data[j].rstrip().lstrip())
                j += 1
            i = j
        if "Subnets" in data[i]:
            j = i + 1
            while j < len(data):
                sub.append(data[j].rstrip().lstrip())
                j += 1
        i += 1

    for i in range(len(nat)+1):
        row = []
        for j in range(len(sub)+1):
            if i == 0:
                if j == 0:
                    row.append('')
                else:
                    row.append(sub[j-1])
            else:
                if j == 0:
                    row.append(nat[i-1])
                else:
                    row.append('0')
        t.append(row)

    j = 1
    while j <= len(sub):
        if len(find_nat_same_zone(nat,get_zone(t[0][j]))) == 0:
            t[find_min(t,j)][j] = '1'
        elif len(find_nat_same_zone(nat,get_zone(t[0][j]))) == 1:
            t[find_nat_same_zone(nat,get_zone(t[0][j]))[0]][j] = '1'
        else:
            t[find_min_same_zone(t,find_nat_same_zone(nat,get_zone(t[0][j])),j)][j] = '1'
        j += 1

    i = 1
    while i <= len(nat):
        print('Instance (' + t[i][0] + '):')
        j = 1
        while j <= len(sub):
            if t[i][j] == '1':
                print(' subnet (' + t[0][j] + ')')
            j += 1
        i += 1

if __name__ == "__main__":
    main()