The Journey of a Web Request: Understanding the Anatomy of Typing “https://www.google.com" in Your Browser
Bassant Aboelhassan
Bassant Aboelhassan

4 min read
·
Just now





Introduction: Have you ever wondered what happens behind the scenes when you type a URL like “https://www.google.com" into your web browser and hit Enter? In this blog post, we’ll take a deep dive into the journey of a web request, covering each step from the initial DNS lookup to the final rendering of the webpage.

DNS Request:


The process begins with a Domain Name System (DNS) lookup. Your browser sends a DNS request to a DNS server to translate the human-readable domain name “www.google.com" into an IP address. The DNS server then responds with the IP address associated with the domain.

TCP/IP:


Once the browser has obtained the IP address of the server hosting the website, it establishes a Transmission Control Protocol (TCP) connection. TCP ensures reliable and ordered delivery of data packets between the client (your browser) and the server.

Firewall:


Before the TCP connection is established, the request may pass through a firewall. Firewalls act as a barrier between your computer and the internet, filtering incoming and outgoing traffic based on predefined security rules. The firewall may inspect the request to ensure it complies with the organization’s security policies.

HTTPS/SSL:


Modern websites often use HTTPS (Hypertext Transfer Protocol Secure) to encrypt data transmitted between the client and the server. When your browser connects to a website using HTTPS, it initiates a secure SSL/TLS handshake. This handshake establishes a secure connection and verifies the authenticity of the server using digital certificates.

Load-Balancer:


Large websites like Google often use load balancers to distribute incoming web traffic across multiple servers. Load balancers improve website performance, scalability, and reliability by evenly distributing the workload among servers.

Web Server:


Once the TCP connection is established and the SSL handshake is completed, your browser sends an HTTP request to the web server. The web server, such as Apache or Nginx, receives the request and processes it. It retrieves the requested resources, such as HTML, CSS, JavaScript files, and images, and prepares the HTTP response.

Application Server:


In some cases, the web server may need to communicate with an application server to generate dynamic content. Application servers execute server-side scripts, interact with databases, and perform other application-specific tasks. For example, when you perform a search on Google, the web server may communicate with an application server to retrieve search results.

Database:


If the requested content is stored in a database, the application server queries the database to retrieve the relevant data. Databases, such as MySQL, PostgreSQL, or MongoDB, store and manage the website’s data, including user information, content, and other resources.

Conclusion: From the initial DNS lookup to the final rendering of the webpage, the journey of a web request involves multiple steps and technologies working together seamlessly. Understanding this process gives us insight into the complex infrastructure behind the websites we interact with every day. Next time you type a URL into your browser, remember the journey your web request takes before the webpage appears on your screen.





