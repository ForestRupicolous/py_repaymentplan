#!/opt/local/bin/python3.6                                                                                                                                 
###################
# Mortgage payment calculator
#from https://www.quora.com/How-do-I-calculate-the-loan-repayment-in-Python
import sys, argparse
    
parser = argparse.ArgumentParser(description="Loan Payment Calculator")
parser.add_argument("-p",   "--principal", type=float, default=106000, help="Principal Loan")
parser.add_argument("-i",   "--interest", type=float, required=True, help="Annual interest rate")
parser.add_argument("-n",   "--number_of_months", type=int, default=240, help="Count of payments")
parser.add_argument("-v",   "--verbosity", action="count", default=0, help="Show monthly balance")
args = parser.parse_args()
verboseMode = args.verbosity
MortgageAPR = args.interest
PrimaryLoan = args.principal
LoanTerm = args.number_of_months
    
irate = ((1+MortgageAPR/100.0) ** (1.0/12)) - 1
MonthlyPmnt = PrimaryLoan * (irate * ((1+irate) ** LoanTerm)) / (((1+irate) ** LoanTerm) - 1)
print ("Monthly payment is", '{:.2f}'.format(MonthlyPmnt), "for loan of", PrimaryLoan, \
                "paid back in", LoanTerm, "months at a fixed APR of", '{:.4f}'.format(MortgageAPR), \
                    'results in a sum of ','{:.2f}'.format(LoanTerm*MonthlyPmnt))
    
if verboseMode == 0:
    print ("Use the -v option for a list of monthly loan balance and equity over these", LoanTerm, "months")
else:
    BalanceOfLoan = PrimaryLoan
    print ("Npmnt     Loan       Equity      Pct")
    for k in range (LoanTerm):
        NpaymentsMade = k+1
        BalanceOfLoan = BalanceOfLoan * (1+irate) - MonthlyPmnt
        EquityInProperty = PrimaryLoan - BalanceOfLoan
        print ('%4d %12.2f %12.2f %6.2f' % (NpaymentsMade, BalanceOfLoan, EquityInProperty, 100*(EquityInProperty/PrimaryLoan)))
sys.exit(0)