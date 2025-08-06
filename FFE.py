import math as m
import numpy as np
def future_values(PV, r,n):
    FV = PV * (1 + r)**n
    return FV
def Present_values(FV, r, n):
    PV = FV / (1 + r)**n
    return PV
def present_value_annuity(PMT, r, n): 
    PV_annuity = PMT * (1 - (1 + r)**(-n)) / r
    return PV_annuity
def future_value_annuity(PMT, r, n):
    FV_annuity = PMT * ((1 + r)**n - 1) / r 
    return FV_annuity
def main():
    PV = float(input("Enter Present Value (PV): "))
    FV = float(input("Enter Future Value (FV): "))
    PMT = float(input("Enter Payment per period (PMT): "))
    r = float(input("Enter Interest Rate (r in decimal, e.g. 0.05 for 5%): "))
    n = int(input("Enter Number of Periods (n): "))

    calculated_FV = future_values(PV, r, n)
    calculated_PV = Present_values(FV, r, n)
    calculated_PV_annuity = present_value_annuity(PMT, r, n)
    calculated_FV_annuity = future_value_annuity(PMT, r, n)

    print("\n--- Results ---")
    print(f"Future Value (FV) from PV: {calculated_FV:.2f}")
    print(f"Present Value (PV) from FV: {calculated_PV:.2f}")
    print(f"Present Value of Annuity: {calculated_PV_annuity:.2f}")
    print(f"Future Value of Annuity: {calculated_FV_annuity:.2f}")

if __name__ == "__main__":
    main()