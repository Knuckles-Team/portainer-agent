Portainer Business Edition comes with Role-Based Access Control (RBAC) features that refine the access privileges available natively within Portainer. The RBAC feature allows you to create granular user access across all resources and all environments defined within Portainer.
##
[hashtag](https://docs.portainer.io/admin/user/roles#the-basics)
The basics
  * A _role_ is a predefined set of privileges.
  * _Privileges_ define the rights to perform actions.
  * Users are assigned roles, and each role has specific privileges.
  * To assign privileges, pair a user or team with a role then associate that pairing with an environment or environment group.
  * A single user or team can have different roles for different environments in the Portainer inventory.


##
[hashtag](https://docs.portainer.io/admin/user/roles#built-in-roles)
Built-in roles
There are several types of roles:
  * **Environment administrator** has full access within a given environment, but cannot make any changes to the infrastructure that underpins an environment (i.e. no host management), nor are they able to make changes to Portainer internal settings. Environment administrators are also unable to change ownership of resources.
  * **Edge administrator** has full control over all resources in all Edge environments, and access to the Edge Compute features.
  * **Operator** has operational control over the resources deployed within a given environment. Operator can update, re-deploy, start and stop containers/services, check logs and console into containers, but cannot create or delete any resources.
  * **Helpdesk** has read-only access to the resources deployed within a given environment but cannot make changes to any resource, nor can they open a console to a container or make changes to a container’s volumes.
  * **Namespace Operator** has operational control over all existing resources in a namespace of an environment. This is similar to the Operator role, but restricted to specified namespaces instead of the entire environment, and is only available for Kubernetes environments.
  * **Standard User** has complete control over the resources that a user deploys, or if the user is a member of a team, has complete control over the resources that users of that team deploy.
  * **Read-Only User** has read-only access to the resources they are entitled to see (resources created by members of their team, and public resources).


![](https://docs.portainer.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FxdTQRpMuktD2l0URtOJO%2Fblobs%2FnRmbGjBMp4Y8cFKfuD2O%2F2.29-admin-user-roles.png&width=768&dpr=3&quality=100&sign=fa567d41&sv=2)
The **Administrator** role sits outside of the other roles and effectively acts as a 'Global Admin'. A user assigned to this role has complete control over Portainer settings, and all resources on every environment under Portainer's control.
circle-info
The **Team Leader** role (which can be defined when [adding a new team](https://docs.portainer.io/admin/user/teams/add)) is designed for setups that are using internal authentication only, and in a future version the role will be disabled when external authentication is enabled.
##
[hashtag](https://docs.portainer.io/admin/user/roles#viewing-user-access)
Viewing user access
Portainer's **Effective access viewer** lets you see what access a user has. From the menu expand **User-related** then select **Roles**.
![](https://docs.portainer.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FxdTQRpMuktD2l0URtOJO%2Fblobs%2FiHeyeBVi55dH1PORhyvk%2FRoles-page-new.gif&width=768&dpr=3&quality=100&sign=3f44ea3e&sv=2)
Scroll down to the **Effective access viewer** section and select a user from the **User** dropdown. The user's roles and their access on your environments will display. Select **Manage access** on any row to be taken to the [environment's access configuration](https://docs.portainer.io/admin/environments/environments#manage-access).
![](https://docs.portainer.io/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FxdTQRpMuktD2l0URtOJO%2Fblobs%2F7BMri2TYgjNW4LaNtExL%2F2.15-settings-users-roles-access.png&width=768&dpr=3&quality=100&sign=e151a3f0&sv=2)
##
[hashtag](https://docs.portainer.io/admin/user/roles#docker-vs-kubernetes)
Docker vs Kubernetes
Because Docker does not natively provide role-based access control, we implement our own role management in order to provide this functionality. On a Kubernetes environment, we leverage the RBAC functionality built into Kubernetes alongside our own role management to provide security and flexibility to roles and access.
For more information on the permissions that each role has for Docker and Swarm environments, see our [Docker roles and permissions documentation](https://docs.portainer.io/advanced/docker-roles-and-permissions). For more information about how we map Portainer roles to Kubernetes roles, see our [roles and bindings documentation](https://docs.portainer.io/advanced/kubernetes-roles-and-bindings).
[PreviousAdd a user to a teamchevron-left](https://docs.portainer.io/admin/user/teams/add-user)[NextEnvironment-relatedchevron-right](https://docs.portainer.io/admin/environments)
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.portainer.io/privacy-policy).
close
AcceptReject
