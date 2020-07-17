# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

# do not use regex here! 

def fun(s: str):
    try:
        name, address = s.split('@')
        site, extension = address.split('.')
    except:
        return False
    
    name = name.replace('-', '').replace('_','')
    if name.isalnum() == False: return False
    if len(extension) > 3: return False
    if site.isalnum() == False: return False
    else:
        return True


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

