def save_accounts_to_file():
    with open('account_info.py', 'w') as f:
        f.write('insert_file_name = {\n')
        for acc_num, acc_details in insert_dict_name.items():
            f.write(f'    {acc_num}: {acc_details},\n')
        f.write('}\n')
    print("Accounts updated and saved to 'accounts.py'")