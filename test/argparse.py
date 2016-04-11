# import argparse
#
# parser = argparse.ArgumentParser(description='Short sample app')
#
# parser.add_argument('-a', action="store_true", default=False)
# parser.add_argument('-b', action="store", dest="b")
# parser.add_argument('-c', action="store", dest="c", type=int)
#
# print parser.parse_args(['-a', '-bval', '-c', '3'])

# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument('num')
# args = parser.parse_args()
#
# print(int(args.num)**2)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('num', type=int, nargs='+')
parser.add_argument('-M', '--max', dest='main', action='store_const',
                    const=max, default=sum)
parser.add_argument('-m', '--min', dest='main', action='store_const',
                    const=min, default=sum)
args = parser.parse_args()

print(args.main(args.num))