import re
def main():
    text='N900001'
    pattern=re.compile(r'N+(\d{7})')
    if pattern.search(text):
        print(True)
    else:
        print(False)

main()