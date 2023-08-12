## ATM and Card Servicing Outage Incident Report
The following is the incident report for the ATM and card servicing outage that occurred between May 15 and May 16, 2023.

![postmortem image](https://www.splunk.com/content/dam/splunk-blogs/images/en_us/2022/07/incident-repsonse1.png)

### Issue Summary

From 9:13 PM to 7:00 AM(East African Time, UTC+3), ATM and card transactions resulted in 503 error messages. This outage affected multiple ATMs and card services provided to Diamond Trust Bank due to configuration errors in networking components provided by our third party service.

### Timeline(All East African Time)
* **9:00**: Configuration push begins.
* **9:13**: Outage begins.
* **9:20**: Pagers alerted the Contact Center Team.
* **9:30**: Contact Center send escalation calls and emails to Service Engineers.
* **12:00**: Engineers acknowledge to the escalation request.
* **12:30**: Initial assessment suggested network issues, network logs reviewed for anomalies.
* **12:45**: Suspicion arose regarding configuration discrepancies in the networking components.
* **1:00**: Network configuration audit initiated to identify misconfigurations or any other anomalies.
* **2:00**: Audit revealed improper settings in the network switch's routing table.
* **2:30**: Load balancer logs analyzed, indicating uneven distribution of traffic.
* **3:00**: Misconfigured switch identified as the root cause of traffic redirection.
* **3:10**: Incident escalated to the vendor responsible for network management.
* **4:00**: Vendor acknowledges the pager.
* **4:30**: Vendor acknowledged configuration errors and started corrective actions.
* **6:00**: Successful configuration change rollback
* **6:30**: Server restarts begin
* **7:00**: Services restored.

### Root Cause

The root cause of the outage was identified as configuration errors in the network switch managed by our third-party service. The network switch's routing table was configured incorrectly, leading to improper redirection of traffic. This caused an overload on the load balancer, disrupting ATM and card services.

### Resolution and Recovery

At 9:13 PM, the monitoring systems alerted the contact center of the outage who quickly escalated the issue to the responsible teams. Reaching the engineers was quite a tussle but at 12:00 midnight they were finally able to reach them.

At 12:30 the initial assessment suggested network issues after an attempt to rollback configuration change. The Engineers corrected the misconfigured settings in the network switch's routing table. Load balancer configurations were also adjusted to ensure proper traffic distribution and at 6:00 AM a successful rollback was achieved which upon completion of these corrective actions, ATM and card services were fully restored.

### Corrective and Preventative Measures

For about a week now, we have been doing internal review and analysis of the outage. The following are the steps we are taking to ensure that the same issue doesn't reoccur.

1. **Configuration Review**: Conduct a thorough review of all networking components' configurations to identify and rectify potential misconfigurations.
2. **Automated Audits**: Implement regular automated audits of network settings to promptly detect configuration errors.
3. **Redundancy Enhancement**: Strengthen redundancy mechanisms to distribute traffic evenly in case of misconfigurations.
4. **Vendor Collaboration**: Establish a communication channel for efficient escalation and resolution with third-party vendors.
5. **Documentation Update**: Maintain up-to-date documentation for network configurations to facilitate quicker incident resolution.
6. **Load Testing**: Conduct load testing to assess the impact of configuration changes and prevent potential service disruptions.

We deeply apologize for the inconvenience caused by this incident and assure you that we are committed to implementing the necessary measures to prevent similar issues in the future. We value your partnership and appreciate your understanding as we work to enhance the reliability and stability of our services.
