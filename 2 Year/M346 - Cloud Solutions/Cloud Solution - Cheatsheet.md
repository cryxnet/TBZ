
> Lernziele: https://gitlab.com/ch-tbz-it/Stud/m346/m346/-/blob/main/KN00/KN00.md

## Cloud-init

- Cloud-init is open-source software used to automate the configuration and initialization of virtual machines in cloud computing environments. It allows administrators to define user data instructions that automate tasks such as software installation, network configuration, and user account setup.

```yaml
#cloud-config
# Sets the hostname of the virtual machine to "my-vm".
hostname: my-vm
# Sets the fully qualified domain name (FQDN) of the virtual machine to "my-vm.example.com".
fqdn: my-vm.example.com
# Adds a new user named "ubuntu", adds dand authorizes SSH access with an SSH public key.
users:
  - name: ubuntu # name
    sudo: ALL=(ALL) NOPASSWD:ALL # give all sudo and no pwd req
    groups: users, admin # adds to grouü
    home: /home/ubuntu # allocate home dir
    shell: /bin/bash # allocates the shell
    ssh_authorized_keys:
      - ssh-rsa keykeykey aws-key
ssh_pwauth: true # enable pw auth
disable_root: false # disables root
# Installs the Nginx web server and Git version control system.
packages:
  - nginx
  - git
# Creates an Nginx configuration file for the virtual host "my-vm.example.com".
write_files:
  - content: |
      server {
          listen 80;
          server_name my-vm.example.com;

          location / {
              root /var/www/my-app;
              index index.html;
          }
      }
    path: /etc/nginx/sites-available/my-vm.conf
    owner: root:root
    permissions: '0644'
# Creates a simple HTML file for the virtual host "my-vm.example.com".
  - content: |
      <!DOCTYPE html>
      <html>
      <body>
      <h1>Welcome to my app!</h1>
      </body>
      </html>
    path: /var/www/my-app/index.html
    owner: www-data:www-data
    permissions: '0644'
# Restarts the Nginx web server to apply the new configuration, clones a Git repository, and sets the correct permissions for the web server directory.
runcmd:
  - systemctl restart nginx
  - git clone https://github.com/my-user/my-app.git /var/www/my-app
  - chown -R www-data:www-data /var/www/my-app
```

**Pro Arguments:**
1.  **Automation:** Cloud-init enables automated provisioning and configuration of virtual machines, reducing the need for manual setup and configuration. This improves efficiency and reduces the risk of errors and inconsistencies.
2.  **Flexibility:** Cloud-init can be used with a variety of cloud providers, operating systems, and virtual machine images. This provides organizations with the flexibility to use their preferred cloud provider and customize their virtual machine images to meet their specific requirements.
3.  **Security:** Cloud-init supports several security features, such as password hashing and SSH key authentication. This helps to ensure that virtual machines are secure and protected from unauthorized access.
4.  **Standardization:** Cloud-init provides a standardized way of configuring virtual machines, making it easier to manage and maintain infrastructure resources. This reduces the risk of configuration drift and helps to ensure consistency across virtual machines.

## Infrastructure as Code
- Infrastructure as Code (IaC) is a practice of defining and managing infrastructure resources such as virtual machines, networks, and storage using machine-readable configuration files. It allows for automated provisioning, deployment, and scaling of infrastructure resources, enabling organizations to treat their infrastructure as software. This approach increases efficiency, reduces errors, and facilitates collaboration among teams.
-   AWS CloudFormation: A service that allows users to define and manage infrastructure resources in AWS using YAML or JSON templates.
-   Azure Resource Manager: A service that enables users to define and manage infrastructure resources in Azure using JSON templates.
-   Google Cloud Deployment Manager: A service that allows users to define and manage infrastructure resources in Google Cloud Platform using YAML or Python templates.
-   HashiCorp Terraform: A tool that provides a declarative way to define and manage infrastructure resources across multiple cloud providers and on-premises environments.
-   Ansible: An open-source automation tool 

## Virtualization
- Virtualization is the process of creating a virtual version of a physical resource, such as a server, storage device, or network, using software. Virtualization enables multiple virtual resources to run on a single physical resource, which can improve resource utilization, increase flexibility, and reduce costs. Examples of virtualization include server virtualization, network virtualization, and storage virtualization.

### Hypervisor
- The hypervisor is a piece of software that creates and manages virtual machines on a physical host. It abstracts the underlying physical resources and presents them as virtual resources to the guest operating systems running on the virtual machines. The hypervisor also manages the allocation of physical resources to virtual machines, ensuring that each virtual machine has access to the resources it needs to run.
![[Pasted image 20230407192414.png]]

#### Type 1
- **Type 1 hypervisors:** Also known as bare-metal hypervisors, Type 1 hypervisors run directly on the host's hardware, without the need for an underlying operating system. They provide direct access to the physical resources, such as CPU, memory, and storage, and can support multiple guest operating systems running on virtual machines. Examples of Type 1 hypervisors include VMware ESXi, Microsoft Hyper-V, and Citrix Hypervisor.

#### Type 2
- **Type 2 hypervisors:** Also known as hosted hypervisors, Type 2 hypervisors run on top of an existing operating system, such as Windows, Linux, or macOS. They rely on the underlying operating system to manage access to the physical resources and provide virtualization capabilities to guest operating systems running on virtual machines. Examples of Type 2 hypervisors include Oracle VirtualBox, VMware Workstation, and Parallels Desktop.

### Hyperscalers
- A hyperscaler is a cloud service provider that operates at a massive scale, providing cloud-based services to millions of users worldwide. Examples include Amazon Web Services, Microsoft Azure, Google Cloud Platform, and IBM Cloud. They offer massive amounts of compute, storage, and network resources at low costs, thanks to economies of scale and efficient resource utilization.

## Usage models

### Public vs. Privat Cloud
1.  **Private Cloud:** A private cloud is a cloud computing environment that is owned, operated, and dedicated to a single organization. Private clouds can be located on-premises or hosted by a third-party service provider. They are typically used by organizations that require more control over their computing resources, greater customization, and higher levels of security and privacy. Private clouds are not shared with other organizations, and access is restricted to authorized personnel.

2.  **Public Cloud:** A public cloud is a cloud computing environment that is owned and operated by a third-party cloud provider and is available to the general public or a large industry group. Public clouds are typically used by organizations that require high scalability, rapid deployment, and lower costs. Public clouds are shared with other organizations and can be accessed over the internet. Access is usually provided through a web-based interface or API, and pricing is typically based on usage.

3. **Hyprid Cloud:** A hybrid cloud is a cloud computing environment that combines both public and private cloud resources. It allows companies to leverage the benefits of both cloud models, such as the scalability and cost-effectiveness of the public cloud, while also maintaining control over sensitive data and applications in a private cloud. This enables businesses to optimize their IT infrastructure and resources to meet their specific needs and requirements.

## Service models
### Cloud-System Layers
- ![[Infrastructure as a Service (IaaS)]]
- ![[Platform as a Service (PaaS)]]
- ![[Function as a Service (FaaS)]]
- ![[Software as a Service (SaaS)]]

## (Cloud-) Migrations models
Migration models are strategies for moving an organization's data, applications, and infrastructure from one environment to another. There are several migration models, including lift and shift, re-platforming, and refactoring.

1.  Lift and shift: This model involves moving an application or system from one environment to another without making any significant changes to its architecture or functionality. This means the application or system will function in the same way as before but on a different infrastructure. It is often used when the primary objective is to migrate quickly and with minimal disruption.

2.  Re-platforming: This model involves migrating an application or system to a new environment with some changes made to its architecture or functionality. The aim of re-platforming is to take advantage of the features and benefits of the new environment. For example, migrating a system from on-premise to the cloud could involve changes to its architecture to make it more cloud-friendly.
 
3.  Refactoring: This model involves migrating an application or system to a new environment and making significant changes to its architecture and functionality to optimize it for the new environment. This approach often involves rewriting or redesigning parts of the application or system to take full advantage of the new environment's features and benefits. For example, migrating a monolithic application to a microservices architecture could involve significant changes to the application's design and functionality.

## Storage models

### Storage service
1.  Object Storage: Object storage is a type of storage architecture that manages data as objects, each with its own unique identifier, metadata, and data. Object storage is ideal for storing large amounts of unstructured data such as images, videos, audio files, and documents. Object storage is highly scalable and designed to be accessed over the network. (Amazon S3)
    
2.  Block Storage: Block storage is a type of storage architecture that stores data in fixed-sized blocks. Each block has its own address and can be accessed independently. Block storage is commonly used in enterprise applications such as databases and virtual machines. Block storage provides high performance and low latency, making it ideal for applications that require fast access to data. (Amazon Elastic Block Store)
    
3.  File Storage: File storage is a type of storage architecture that stores data as files in a hierarchical directory structure. File storage is commonly used in network-attached storage (NAS) systems and is ideal for storing data that needs to be shared across multiple users or applications. File storage provides a high level of compatibility with existing applications and operating systems. (Amazon Elastic File System)
    
4.  Tape Storage: Tape storage is a type of storage architecture that stores data on magnetic tape cartridges. Tape storage is commonly used for long-term data archiving and backup purposes, as tape cartridges can hold large amounts of data and are relatively inexpensive. Tape storage is less expensive than disk-based storage but slower to access, making it less suitable for applications that require fast data access. (AWS Storage Gateway-Virtual Tape Library)

### Storage type

Hot, cold, and warm storage are terms used to describe different storage tiers based on the frequency and speed of access to data, as well as the cost of storage.

1. **Hot storage:** refers to the highest performance and fastest access storage tier, where data is frequently accessed and needs to be available at all times. It is typically the most expensive storage tier, and is often used for critical workloads that require low latency and high throughput. Examples of hot storage include solid-state drives (SSDs) and high-performance block storage.

2. **Cold storage:**, on the other hand, is a low-cost storage tier used for data that is accessed infrequently or is rarely modified. It is suitable for data that can be stored offline or on tape, and is ideal for long-term archival purposes. Examples of cold storage include Amazon S3 Glacier and Amazon S3 Glacier Deep Archive.

3. **Warm storage:** is a middle ground between hot and cold storage, providing faster access than cold storage but at a lower cost than hot storage. It is suitable for data that is accessed periodically but not frequently, and is often used for backup and disaster recovery purposes. Examples of warm storage include Amazon S3 Standard-Infrequent Access (S3 Standard-IA) and Amazon EBS Throughput Optimized HDD (st1).

### Persistent and volatile storage
Persistent and volatile storage are two types of storage used in computing, particularly in virtual instances.

- **Persistent storage** refers to non-volatile storage, which means that data is stored even when power is removed. This type of storage is used for long-term data storage and is typically slower than volatile storage. Examples of persistent storage include hard disk drives (HDDs) and solid-state drives (SSDs).

- **Volatile storage**, on the other hand, refers to storage that is lost when power is removed. This type of storage is used for short-term data storage and is typically faster than persistent storage. Examples of volatile storage include random-access memory (RAM) and cache memory.

In the context of virtual instances, persistent storage is used for data that needs to be stored long-term, such as databases, files, and operating system images. Volatile storage, such as RAM, is used for running applications and storing data temporarily while the virtual instance is powered on.

It is important to understand the difference between persistent and volatile storage in virtual instances, as it can affect the performance and availability of applications and data. For example, if a virtual instance relies solely on volatile storage, any data stored in RAM will be lost if the instance is shut down or restarted. Therefore, it is often necessary to use persistent storage to ensure that data is retained even if the instance is powered off or terminated.