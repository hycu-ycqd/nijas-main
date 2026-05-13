import requests
from msal import PublicClientApplication

# --- Config ---
CLIENT_ID = "7f12e0f8-426a-4980-81c5-79a1da19cbda"
TENANT_ID = "dcc67e7e-c0c9-484c-a4ef-9d6609ac1f67"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["Mail.ReadWrite", "MailboxSettings.ReadWrite"]
REDIRECT_URI = "http://localhost"  # Only used for interactive login
USER_ID = "janet@t3l4z.onmicrosoft.com"  # or 'user@example.com'
NEW_FOLDER_NAME = "copy amarnath mails"
SENDER_EMAIL1 = "suhas@t3l4z.onmicrosoft.com"
domain_mail_id = "t3l4z.onmicrosoft.com"

access_token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6InppbnRfX2NsV2w3YlE1dGsxRmhZZUtZMW55cThKcDBYeXlqaWdLTXo1aGsiLCJhbGciOiJSUzI1NiIsIng1dCI6IkNOdjBPSTNSd3FsSEZFVm5hb01Bc2hDSDJYRSIsImtpZCI6IkNOdjBPSTNSd3FsSEZFVm5hb01Bc2hDSDJYRSJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9kY2M2N2U3ZS1jMGM5LTQ4NGMtYTRlZi05ZDY2MDlhYzFmNjcvIiwiaWF0IjoxNzQ1ODUxNzU4LCJuYmYiOjE3NDU4NTE3NTgsImV4cCI6MTc0NTg1NTY1OCwiYWlvIjoiazJSZ1lDaUo4MTFlLzVGeDJ3WG0xM2VPOTRhZkFRQT0iLCJhcHBfZGlzcGxheW5hbWUiOiJBcHAgZm9yIEVYTyAtIENoaXQxIiwiYXBwaWQiOiJhNTU2YjI0My1hMWJkLTQyOTktYTIyNS1iZWNlMTBkMzE4ZTkiLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9kY2M2N2U3ZS1jMGM5LTQ4NGMtYTRlZi05ZDY2MDlhYzFmNjcvIiwiaWR0eXAiOiJhcHAiLCJvaWQiOiJlNTg3ZWQ0Mi00YWJlLTQ3ZTEtYmE4OC00N2M2NDNmMGVkOTYiLCJyaCI6IjEuQWNZQWZuN0czTW5BVEVpazc1MW1DYXdmWndNQUFBQUFBQUFBd0FBQUFBQUFBQURHQUFER0FBLiIsInJvbGVzIjpbIk1haWwuUmVhZFdyaXRlIiwiVXNlci1NYWlsLlJlYWRXcml0ZS5BbGwiLCJVc2VyLlJlYWRXcml0ZS5BbGwiLCJNYWlsYm94SXRlbS5SZWFkLkFsbCIsIkRpcmVjdG9yeS5SZWFkV3JpdGUuQWxsIiwiTWFpbGJveFNldHRpbmdzLlJlYWQiLCJDb250YWN0cy5SZWFkV3JpdGUiLCJHcm91cC5SZWFkV3JpdGUuQWxsIiwiTm90ZXMuUmVhZC5BbGwiLCJNYWlsYm94SXRlbS5JbXBvcnRFeHBvcnQuQWxsIiwiVXNlci5SZWFkLkFsbCIsIlRhc2tzLlJlYWQuQWxsIiwiTWFpbGJveEZvbGRlci5SZWFkV3JpdGUuQWxsIiwiTWFpbC5SZWFkIiwiQ2FsZW5kYXJzLlJlYWRXcml0ZSIsIkFjY2Vzc1Jldmlldy5SZWFkLkFsbCIsIk1haWwuU2VuZCIsIk1haWxib3hTZXR0aW5ncy5SZWFkV3JpdGUiLCJHcm91cE1lbWJlci5SZWFkV3JpdGUuQWxsIiwiQ29udGFjdHMuUmVhZCIsIlRhc2tzLlJlYWRXcml0ZS5BbGwiLCJOb3Rlcy5SZWFkV3JpdGUuQWxsIl0sInN1YiI6ImU1ODdlZDQyLTRhYmUtNDdlMS1iYTg4LTQ3YzY0M2YwZWQ5NiIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJBUyIsInRpZCI6ImRjYzY3ZTdlLWMwYzktNDg0Yy1hNGVmLTlkNjYwOWFjMWY2NyIsInV0aSI6IjVZX0JPY1N1cTAteEYxQzdQNndSQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbIjA5OTdhMWQwLTBkMWQtNGFjYi1iNDA4LWQ1Y2E3MzEyMWU5MCJdLCJ4bXNfaWRyZWwiOiI4IDciLCJ4bXNfdGNkdCI6MTczOTQ5NDY5MH0.LEG-2qb5rzA9Gcc230q3CToid58zEchV0BTbltdtdQWHSlRcZJhxjIeWPkjOqor6CimEruhx91oCv3AMdTgitSV33SODQopa-YR6aJNd95ISGdG5DH-7rlOHnxQ4GXN-jEU4XanIg2BlT-sGGUHCBIGLO6T6WLqdiOTU9YNKCmOPJHPEn_fsfvH5BdD-3mSgS28eKVDoCLQYYtSp5_1doEVTJsHcNvJS7Se9aolhW4fxaw6_m3LvnEtP3Gg-yZpFqN_PPd5SMLxSDa_DlctqKdwEuEd3UOdzlEJGGaJUBDfKyHAyV6VTb7E055v_pcU_SqkrunxrjKlwZ7T2wQe1EA"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

mail_list = ["janet", "kurdush","scalesharedmailbox", "lovish", "suhas"]
for SENDER_EMAIL1 in mail_list:
    SENDER_EMAIL = SENDER_EMAIL1 + "@" + domain_mail_id

    for type in ["copyToFolder", "moveToFolder"]:
        NEW_FOLDER_NAME = SENDER_EMAIL1 + " mails " + type
        # --- Step 1: Create Folder ---
        create_folder_url = f"https://graph.microsoft.com/v1.0/users/{USER_ID}/mailFolders"
        folder_data = { "displayName": NEW_FOLDER_NAME }

        folder_response = requests.post(create_folder_url, headers=headers, json=folder_data)

        if folder_response.status_code != 201:
            raise Exception(f"❌ Failed to create folder: {folder_response.text}")

        folder_id = folder_response.json()["id"]
        print(f"✅ Folder '{NEW_FOLDER_NAME}' created with ID: {folder_id}")

        # --- Step 2: Create Inbox Rule to Move Messages to Folder ---
        rules_url = f"https://graph.microsoft.com/v1.0/users/{USER_ID}/mailFolders/inbox/messageRules"

        rule_data = {
            "displayName": f"Move emails from {SENDER_EMAIL}",
            "sequence": 1,
            "isEnabled": True,
            "stopProcessingRules": False,
            "conditions": {
                "senderContains": [SENDER_EMAIL]
            },
            "actions": {
                type: folder_id
            }
        }

        rule_response = requests.post(rules_url, headers=headers, json=rule_data)

        if rule_response.status_code == 201:
            print("✅ Rule created successfully")
        else:
            print(f"❌ Failed to create rule: {rule_response.status_code} {rule_response.text}")
