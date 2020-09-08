---
layout: doc
---

# Integrate G Suite Directory

INSERT SUMMARY OF INTEGRATION
  
*  DESCRIBE YOUR SOLUTION. No need to be overly formal, make this section your own.

*  INSERT HIGH LEVEL SUMMARY OF USE CASES THIS MICROAPP ADDRESSES INCLUDING THE KEY WORKFLOWS OF ALL MICROAPPS. WHO CAN DO WHAT. FOR EXAMPLE: This integration delivers actionable notifications to item managers about their items, and enables viewing and editing items directly from Workspace.
  
*  INSERT SUMMARY OF STEPS TO SET UP THE INTEGRATION (HIGH-LEVEL, UP TO ADDING THE INTEGRATION TO MICROAPPS)
  
For comprehensive details about the microapps, see the section below.

## Review prerequisites

After you set up this integration with G Suite Directory, you will need these artifacts to add the integration in Citrix Workspace Microapps:

*  INSERT BULLET POINT LIST OF PARAMETER REQUIREMENTS FOR AUTH
*  INSERT BASE URL
*  INSERT TOKEN URL
*  INSERT AUTHORIZATION URL
*  INSERT USERNAME
*  INSERT PASSWORD
*  INSERT CLIENT ID
*  INSERT SECRET

>**Note:**
>
>It is recommended that you always use OAuth 2.0 as your service authentication method where available. OAuth 2.0 ensures that your integration meets the maximum security compliance with your configured microapp.

The integration requires regular access to your G Suite Directory instance, so we recommend creating a dedicated user account. This account must have the following permissions:

*  INSERT LIST OF ACCESS REQUIREMENTS FOR SERVICE ACCOUNT
*  INSERT ADDITIONAL CONTEXT/LINKS ABOUT ACCOUNT CONFIGURATION

The number of API requests that can be made to specific resources is limited, we therefore recommend the following:

*  INSERT LINK TO API LIMIT DOCUMENTATION
*  INSERT DETAILS ABOUT RECOMMENDED API PLANS

For Workspace authentication we recommend the following:
 *  INSERT DETAILS ON AUTH RECOMMENDATIONS

INSERT DETAILS ON ANY OTHER PRE-REQUISITES INCLUDING LICENSES, API VERSIONS, ETC

## Set up the G Suite Directory integration

INSERT STEPS (SPLIT INTO RELEVANT SUBSECTIONS) REQUIRED TO PREPARE THE SOR FOR THE INTEGRATION
*  INSERT DETAILS ON HOW TO ENABLE APIS
*  INSERT DETAILS ON HOW TO CONFIGURE OAUTH CLIENT
*  INSERT DETAILS ON HOW TO CONFIGURE CALLBACK URLS
*  INSERT DETAILS ON HOW TO CREATE A NEW SERVICE ACCOUNT
*  INSERT DETAILS ON ANY OTHER REQUIRED CUSTOMIZATION


## Add the integration to Citrix Workspace Microapps

Add the G Suite Directory integration to Citrix Workspace Microapps to connect to your application. This delivers out-of-the-box microapps with pre-configured notifications and actions which are ready to use within your Workspace.

**Follow these steps:**

1.  From the **Microapp Integrations** page, select **Add New Integration**, and **Add a new integration from Citrix-provided templates**.
1.  Choose the G Suite Directory tile.
1.  Enter a name for the integration.

INSERT DETAILS ABOUT CONFIGURING THE INTEGRATION AND WHAT PARAMETERS TO ENTER WHERE (SHOULD INCLUDE IMAGES)

1.  Enter the **Service Authentication** and **Connector parameters** that you collected in the previous procedures.
*  INSERT DETAILS ABOUT WHAT PARAMETERS TO ENTER/SELECT

The **Microapp Integrations** page opens with your added integration and its microapps. From here you can add another integration, continue setting up your out-of-the-box microapps, or create a new microapp for this integration.

You are now ready to set and run your first data synchronization. As a large quantity of data can be pulled from your integrated application to the Microapps platform, we recommend you use the **Table** page to filter entities for your first data synchronization to speed up synchronization.

For more information, see [Verify needed entities](/en-us/citrix-microapps/set-up-template-integrations.html#verify-needed-entities) and [Set data synchronization](/en-us/citrix-microapps/set-up-template-integrations.html#set-data-synchronization) in the Configure the integration article.

## Use G Suite Directory microapps

Existing application integrations come with out-of-the-box microapps. Start with these microapps and customize them for your needs.

INSERT TABLE WITH THE LIST OF PAGES/NOTIFICATIONS IN EACH MICROAPP FOLLOWING THE MODEL BELOW. COPY FOR EACH MICROAPP. REMEMBER, THIS IS ACCEPTANCE CRITERIA FOR ADMINS DEPLOYING YOUR MICROAPPS.
  
**YOUR MICROAPP NAME:** WHAT DOES THE MICROAPP DO. FOR EXAMPLE: View and edit your items. Send notifications for updated and expiring items.

|Notification or Page|Use-case workflows|
|:-------------|:-------------|
| NOTIFICATION NAME. FOR EXAMPLE: Item updated notification | WHAT TRIGGERS THE NOTIFICATION AND WHO RECEIVES THE NOTIFICATION. FOR EXAMPLE: When a detail of an item is changed, the owner of the item receives a notification.  |
| NOTIFICATION NAME. FOR EXAMPLE: Expiring item notification | WHAT TRIGGERS THE NOTIFICATION AND WHO RECEIVES THE NOTIFICATION. FOR EXAMPLE: When an item passes a defined threshold before or after its end date (for example, 3 days by default), the owner receives a notification reminder. |
| PAGE NAME. FOR EXAMPLE: Item page | WHAT ACTION DOES THE PAGE ALLOW AND INFORMATION DOES IT PROVIDE. FOR EXAMPLE: Provides a detailed view of an item including contacts and a link to contact details. |
| PAGE NAME. FOR EXAMPLE: Edit Item page | WHAT ACTION DOES THE PAGE ALLOW AND INFORMATION DOES IT PROVIDE. FOR EXAMPLE:FOR EXAMPLE: Provides a form for submitting edits to an item. |
