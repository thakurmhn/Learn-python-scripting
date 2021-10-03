import boto3

iam_res=boto3.resource('iam')
iam_cli=boto3.client('iam')

def iam_create_user(username=''):
    user=iam_res.create_user(UserName=username)
    print(f"Created New IAM Ueser {user.name}")


def iam_delete_user(username=''):
    iam_cli.delete_user(UserName=username)
    print(f"Deleted IAM user {username}")

def iam_list_users():
    for each_user in iam_res.users.all():
        print(each_user)

def Usage():
    # Create User

    try:
        username='test_user2'
        iam_create_user(username)
    except Exception as e:
        print(f"{username} Alreay exist")
        print(f"Deleting user {username}")
        iam_delete_user(username)
    finally:
        iam_create_user(username)
        print("\nFinal list of Users\n")
        iam_list_users()

if __name__ == '__main__':
    Usage()