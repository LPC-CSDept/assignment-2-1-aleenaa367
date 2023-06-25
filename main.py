def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    male = input("Male value: ")
    female = input("Female value: ")
    total = int(male)+int(female)
    print("The total number of students: ", total)
    print(f"The number of males and females \t {male} \t {female}")
    m_perc = (int(male)/total) * 100
    f_perc = (int(female)/total) * 100
    print(f'The percentage of males and females \t {m_perc:.2f}% \t {f_perc:.2f}%')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc



if __name__ == '__main__':
    main()
