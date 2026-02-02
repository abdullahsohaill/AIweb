# Permit.io
**URL:** https://www.permit.io
**Page Title:** Permissions for The AI Era | Permit.io
--------------------


## End-to-end authorization platform anyone can use

## A no-code authorization platform anyone can use.

- Allow your entire team - from devs to sales, to securely manage permissions
Allow your entire team - from devs to sales, to securely manage permissions
- The only solution with a no-code policy editor. Supports any model - RBAC, ABAC and ReBAC.
The only solution with a no-code policy editor. Supports any model - RBAC, ABAC and ReBAC.
- Permit generates fully transparent policy as code based on OPA's Rego or AWS' Cedar
Permit generates fully transparent policy as code based on OPA's Rego or AWS' Cedar
- Everything is managed as code in Git and controlled with a simple API
Everything is managed as code in Git and controlled with a simple API
Permit CLI

## Developer-First Integrated Authorization

Author, Automate, Test, and Deploy Authorization Policies Directly from the Command Line
[LINK: Read the Docs](https://github.com/permitio/permit-cli)
[LINK: Read the Docs](https://github.com/permitio/permit-cli)
- RBAC Role based access default allow := false
allow if {
  some role in data.users[input.user].roles
  actions := roles[role][input.resource.type]
  input.action in actions
}
roles["Banker"]["Loan"] := [
	 "View","Approve","Decline"
] Create dynamic Role Based Access Control policies, like: " Banker can Approve Loan " Start with RBAC
RBAC

### Role based access

Create dynamic Role Based Access Control policies, like:
" Banker can Approve Loan "
- ABAC Granular attributes default allow := false
allow if {
  some _, allowed_actions in conditions
  input.action in allowed_actions[input.resource.type]
}
conditions["Weekend Shift Employee"]["Database"] := [
	 "Read", "Update", "Backup", "Restore"
] if {
	 work_days := { day |
    day := data.users[input.user].attributes.work_days[_]
  }
  count({"Saturday", "Sunday"} & work_days) > 0
} Build nuanced attribute based access control policies by adding attributes, like: " Weekend Shift Employees can access Database during Weekend " Learn about ABAC
ABAC

### Granular attributes

Build nuanced attribute based access control policies by adding attributes, like:
" Weekend Shift Employees can access Database during Weekend "
- ReBAC Resource and user hierarchies default allow := false
allow if {
	 patient_caregiver = true
}
patient_caregiver if {
	 user_roles := data.users[input.user].roles
	 some assigned_resource, assigned_roles in user_roles
  some role in assigned_roles
  input.action in roles[role][input.resource.type]
  assigned_resource in resource_relationships
}
resource_relationships[resource] {
  related_resources := graph.reachable(
    full_graph,{input.resource.id}
  )
  some resource in related_resources
}
full_graph[child] := parent if {
	 all_resources := [resource | resource := data.resources[_]]
 	some child, parent_resource in object.union_n(all_resources)
	 parent := [object.get(parent_resource, "parent_id", null)]
}
roles["Caregiver"]["Record"] := ["View", "Update", "Share", "Archive"] Create policies based on relationships between users and resources, like: " Caregiver of a Patient can View Patient's Medical Files " Explore ReBAC
ReBAC

### Resource and user hierarchies

Create policies based on relationships between users and resources, like:
" Caregiver of a Patient can View Patient's Medical Files "
Create dynamic Role Based Access Control policies, like:
" Banker can Approve Loan "
- Seamlessly migrate from any existing authorization solution
Seamlessly migrate from any existing authorization solution
- GitOps and Multi-tenancy available out-of-the-box
GitOps and Multi-tenancy available out-of-the-box

### Secure, event-driven, compliant.

Engines
OPA / Cedar
Policy Updater
OPAL
- All authorization decisions are made on your side with zero latency
All authorization decisions are made on your side with zero latency
- Use sensitive data for authorization decisions, without it ever leaving your VPC/Network
Use sensitive data for authorization decisions, without it ever leaving your VPC/Network
- Permit is always up (+99.99) - but you are not dependent on our availability
Permit is always up (+99.99) - but you are not dependent on our availability
- Compliant with HIPAA, SOC2, and more
Compliant with HIPAA, SOC2, and more
[LINK: Learn more](https://docs.permit.io/overview/how-does-it-work#permits-hybrid-architecture)
Engines
OPA / Cedar
Policy Updater
OPAL

## How the Hybrid Model fits your architecture?

Authorization Elements

### Create and embed

Embed customizable access control elements like User Management, Approval Flows, and Audit Logs directly into your app
[LINK: Audit Logs Access powerful audit logs Enjoy automatically generated audit logs for your app and the permission management control plane, and easily propagate them to any logging solution](https://docs.permit.io/how-to/use-audit-logs/types-and-filtering)
Audit Logs

### Access powerful audit logs

Enjoy automatically generated audit logs for your app and the permission management control plane, and easily propagate them to any logging solution
[LINK: Authorization for Authorization Manage your team's access Manage and audit who can grant, change and revoke permissions within your application's authorization system.](https://docs.permit.io/manage-your-account/workspace-settings/#member-management)
Authorization for Authorization

### Manage your team's access

Manage and audit who can grant, change and revoke permissions within your application's authorization system.
[LINK: Gitops Enjoy true Policy-as-Code Manage your policies in a cloud native GitOps flow, combining application level authorization with infra admissions in a unified policy repo.](https://docs.permit.io/integrations/gitops/overview)
Gitops

### Enjoy true Policy-as-Code

Manage your policies in a cloud native GitOps flow, combining application level authorization with infra admissions in a unified policy repo.

## Got questions? Talk with our devs.

Just listen to what these folks had to say...
- Tal Saiag Granulate Founder & CTO At Granulate we optimize our customers’ most critical systems; as a result, getting access control right is of the highest importance.  Full stack permissions as a service allows our developers to focus on their core product. I was extremely impressed both by Permit.io’s technology and its dedication to customer service.
Tal Saiag
Granulate Founder & CTO
- Matan Bakshi Buzzer.ai Founder & CTO Building authorization for Buzzer’s call-rep on-demand service was a challenging task, but with Permit.io we were able to get it up and running end-to-end in just a few days.
Matan Bakshi
Buzzer.ai Founder & CTO
- Ran Ribenzaft Cisco, Epsagon CTO At Epsagon (acquired by Cisco) we are no strangers to the complexity of microservices. Access control demands of microservices are never-ending , so they require a modern stack that can quickly adapt to the most demanding tech and security needs.
Ran Ribenzaft
Cisco, Epsagon CTO
- Nate Young CIO, Maricopa County Recorder's Office Permit’s intuitive policy editor allows access to complex attribute-based conditions that are robust enough for our developers to use, yet simple enough for our non-technical staff to configure without the need for IT assistance
Nate Young
CIO, Maricopa County Recorder's Office
- Hongbo Miao Tesla Senior Software Engineer Moving to modern authorization for microservices is no easy feat, but OPAL made it easy. When I was learning and exploring replicator solutions for OPA myself in my free time, I found that OPAL is a very mature solution  for the open-policy administration layer and beyond.
Hongbo Miao
Tesla Senior Software Engineer
- Jean Philippe Boul Co-founder & COO Jules AI At Jules we aim to streamline the process of buying/selling recycled materials, and sharing access as part of our portal is an important step to achieve that. Allowing users to share access is both important to get right and hard to do so, we're delighted to have Permit solve this problem for us end to end.
Jean Philippe Boul
Co-founder & COO Jules AI

## Our customers have many stories to tell, hear it from them!

### Join our Community

2938 Members

--------------------