import pandas as pd
import uuid
from variables import *

def concat_and_generate_token_to_csv(array_of_csvs, merchant_name):  # for combining multiple dfs

    df_names = ["df_%d" % (x + 1) for x in range(len(array_of_csvs))]

    for i in range(len(array_of_csvs)):
        df_names[i] = pd.read_csv(array_of_csvs[i])

    if len(array_of_csvs) > 1:
        output_df = pd.concat(df_names, axis=0, ignore_index=True)
    else:
        output_df = pd.read_csv(array_of_csvs[0])
    output_df.drop_duplicates(subset=['user_id'], inplace=True)
    output_df.fillna("", inplace=True)
    output_df.sort_values('lifetime_visit', ascending=False, inplace=True)
    output_df.reset_index(inplace=True)

    if 'token' not in output_df.columns:
        uuids = []
        # output_df.drop(output_df.columns[[4, 5, 6, 7, 8, 9, 10, 11]], axis=1, inplace=True)
        output_df['Seperator_Row'] = ''
        output_df['token'] = None
        for i in range(len(output_df.index)):
            uuid_number = uuid.uuid4()
            if uuid_number in uuids:
                uuid_number = uuid.uuid4()
            userid = output_df.user_id[i]
            token = f'FB_V-{userid}_{uuid_number}'
            output_df.loc[i, 'token'] = token
            uuids.append(uuid_number)

    customer_file_path = f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Processed_CSVs/{merchant_name}.csv'
    print(customer_file_path)
    output_df.to_csv(customer_file_path)

# Remember change merchant name
# concat_and_generate_token_to_csv(original_csvs, merchant_name)

#-----------------------------------------------------------------------------------------------------------------------

def drop_excess_index_columns(merchant_name, columns_to_drop):
    customers_file_location = f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Tracker_in_progress/{merchant_name}_tracker.csv'
    df = pd.read_csv(customers_file_location)
    df.drop(df.columns[columns_to_drop], axis=1, inplace=True)
    df.to_csv(customers_file_location)


# drop_excess_index_columns(merchant_name, [0,1])

#--------------------------------------------------------------------------------------------------------------------

def get_status(merchant_name):
    customers_file_location = f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Tracker_in_progress/{merchant_name}_tracker.csv'
    tracker = pd.read_csv(customers_file_location)
    total_sent = sum(tracker['Message Status'].str.contains('Successfully Sent.*'))
    total = len(tracker.index)
    total_with_issues = sum(tracker['Message Status'].str.contains('cannot.*', case=False)) + sum(
        tracker['Message Status'].str.contains('Unable.*')) + sum(tracker['Message Status'].str.contains('No .*'))
    Est_days_left = (total - total_sent) / 150
    print(
        f'Total sent across all sessions is {total_sent} out of {total}. Unable to send {total_with_issues} users. Estimated days left is {Est_days_left}')

# get_status('WhaleTea')

# ------------------------------------------------------------------------------------------------------------
# change all of old status to new status
def change_msg_status(merchant_name, old_status, new_status):
    customers_file_location = f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Tracker_in_progress/{merchant_name}_tracker.csv'
    df = pd.read_csv(customers_file_location)
    df.loc[(df['Message Status'] == old_status), 'Message Status'] = new_status
    df.drop(df.columns[[0]], axis=1, inplace=True)
    df.to_csv(customers_file_location)


#---------------------------------------------------------------------------------------------------------------

def update_exp_date(merchant_name, extension_length):
    customers_file_location = f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Tracker_in_progress/{merchant_name}_tracker.csv'
    df = pd.read_csv(customers_file_location)
    for i in range(len(df.index)):
        prev_exp = df['expiry_date'][i][5:7]
        new_exp = int(prev_exp) + extension_length
        if new_exp < 10:
            new_exp = '0'+ str(new_exp)
        elif new_exp > 12:
            new_exp = str(new_exp-12)
        else:
            new_exp = str(new_exp)

        df.loc[i, 'expiry_date'] = df['expiry_date'][i][:5] + new_exp + df['expiry_date'][i][7:]

#------------------------------------------------------------------------------------------------------------------