import sys
import "reports/complete_report.py"
import "reports/simple_report.py"

def main(args):
    if args[0] == "" and args[1] == "":
        exit("Verfiquei os argumentos")

    if args[1] == "completo":
        CompleteReport.generate(args[0])
    else:
        SimpleReport.generate(args[0])

if __name__ == "__main__":
    main(sys.argv)