---
layout: doc
---

# Citrix G Suite Directory specifications



# Version Details

INSERT VERSION SUPPORT DETAILS HERE

## Endpoints


POST

    https://accounts.google.com/o/oauth2/auth?access_type=offline&prompt=consent
    https://accounts.google.com/o/oauth2/token
    /v1/users

GET

    /v1/groups
    /v1/users
    /v1/groups/{{groupKey}}/members
    /v1/customer/my_customer/orgunits

DELETE

    /v1/users/{{userKey}}

PUT

    /v1/users/{{userKey}}

## Service Actions

*  **Delete User** - INSERT SERVICE ACTION DESCRIPTION
*  **Update User** - INSERT SERVICE ACTION DESCRIPTION
*  **Create User** - INSERT SERVICE ACTION DESCRIPTION

## Key Entities

The following are the main business entities that this             connector addresses:

*  INSERT LIST OF MAIN BUSINESS ENTITIES

## Entities with Attributes

The following is a full list of entities and their             attributes:

group

*  admin_created: BOOLEAN
*  description: BINARY
*  direct_members_count: INTEGER
*  email: STRING(255)
*  etag: STRING(255)
*  id: STRING(255), FK(member.id)
*  kind: STRING(255)
*  name: STRING(255)

group_aliases

*  value: STRING(255)
*  parent_id: STRING(255), FK(group.id)
*  unique_id: STRING(36)
*  root_id: STRING(255)

group_non_editable_aliase

*  value: STRING(255)
*  parent_id: STRING(255), FK(group.id)
*  unique_id: STRING(36)
*  root_id: STRING(255)

user

*  agreed_to_terms: BOOLEAN
*  archived: BOOLEAN
*  change_password_at_next_l: BOOLEAN
*  creation_time: TIMESTAMP
*  custom_gender: STRING(255)
*  customer_id: STRING(255)
*  etag: STRING(255)
*  gender_address_me_as: STRING(255)
*  gender_type: STRING(255)
*  id: STRING(255), FK(member.id)
*  include_in_global_address: BOOLEAN
*  ip_whitelisted: BOOLEAN
*  is_admin: BOOLEAN
*  is_delegated_admin: BOOLEAN
*  is_enforced_in_2_sv: BOOLEAN
*  is_enrolled_in_2_sv: BOOLEAN
*  is_mailbox_setup: BOOLEAN
*  kind: STRING(255)
*  last_login_time: TIMESTAMP
*  name_family_name: STRING(255)
*  name_full_name: STRING(255)
*  name_given_name: STRING(255)
*  org_unit_path: STRING(255), FK(organization_unit.org_unit_path)
*  primary_email: STRING(255)
*  recovery_email: STRING(255)
*  recovery_phone: LONG
*  suspended: BOOLEAN
*  suspension_reason: STRING(255)
*  thumbnail_photo_etag: STRING(255)
*  thumbnail_photo_url: STRING(255)

user_addresses

*  country: STRING(255)
*  country_code: STRING(255)
*  extended_address: STRING(255)
*  formatted: STRING(255)
*  locality: STRING(255)
*  po_box: STRING(255)
*  postal_code: STRING(255)
*  primary: STRING(255)
*  region: STRING(255)
*  source_is_structured: BOOLEAN
*  street_address: STRING(255)
*  type: STRING(255)
*  parent_id: STRING(255), FK(user.id)
*  unique_id: STRING(36)
*  root_id: STRING(255)

user_aliases

*  value: STRING(255)
*  parent_id: STRING(255), FK(user.id)
*  unique_id: STRING(36)
*  root_id: STRING(255)

user_emails

*  address: STRING(255)
*  custom_type: STRING(255)
*  primary: BOOLEAN
*  type: STRING(255)
*  parent_id: STRING(255), FK(user.id)
*  unique_id: STRING(36)
*  root_id: STRING(255)

user_external_ids

*  type: STRING(255)
*  value: STRING(255)
*  parent_id: STRING(255), FK(user.id)
*  unique_id: STRING(36)
*  root_id: STRING(255)

user_non_editable_aliases

*  value: STRING(255)
*  parent_id: STRING(255), FK(user.id)
*  unique_id: STRING(36)
*  root_id: STRING(255)

user_organizations

*  cost_center: STRING(255)
*  custom_type: STRING(255)
*  department: STRING(255)
*  description: STRING(255)
*  domain: STRING(255)
*  full_time_equivalent: INTEGER
*  location: STRING(255)
*  name: STRING(255)
*  primary: BOOLEAN
*  symbol: STRING(255)
*  title: STRING(255)
*  type: STRING(255)
*  parent_id: STRING(255), FK(user.id)
*  unique_id: STRING(36)
*  root_id: STRING(255)

user_phones

*  custom_type: STRING(255)
*  primary: BOOLEAN
*  type: STRING(255)
*  value: STRING(255)
*  parent_id: STRING(255), FK(user.id)
*  unique_id: STRING(36)
*  root_id: STRING(255)

user_relations

*  type: STRING(255)
*  value: STRING(255)
*  parent_id: STRING(255), FK(user.id)
*  unique_id: STRING(36)
*  root_id: STRING(255)

member

*  group_admin_created: BOOLEAN, IGNORED
*  group_description: BINARY, IGNORED
*  group_direct_members_coun: INTEGER, IGNORED
*  group_email: STRING(255), IGNORED
*  group_etag: STRING(255), IGNORED
*  group_id: STRING(255), FK(group.id)
*  group_kind: STRING(255), IGNORED
*  group_name: STRING(255), IGNORED
*  role: STRING(255)
*  kind: STRING(255)
*  etag: STRING(255)
*  id: STRING(255)
*  type: STRING(255)
*  email: STRING(255)
*  status: STRING(255)

organization_unit

*  description: STRING(255)
*  etag: STRING(255)
*  kind: STRING(255)
*  name: STRING(255)
*  org_unit_id: STRING(255)
*  org_unit_path: STRING(255)
*  parent_org_unit_id: STRING(255), FK(organization_unit.org_unit_id)
*  parent_org_unit_path: STRING(255)

