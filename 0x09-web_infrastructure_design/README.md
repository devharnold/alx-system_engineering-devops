This is a well detailed README of how the Simple Web Infrastructure is according to our architect


    Simple-Web-Stack
We have servers that are physical machines or virtual programmes that serve or provide functionality 
to other programmes or clients.
Servers are usually stored in data centres racks(piled on each other)
Virtual programmes are virtual representation of physical servers whereby they have their own Operating Systems

    Domain Name
Replaces the complex IP addresses numbers into easily understandable and replacable form.

    Web Server
Ensure possibility of Web Hosting
The Web server stores files of a site and showcases them on the net so they can be visited by users in the web.
It stores and transmits data via network system -> internet.
Web Servers store and transmit data from a site as requested by a visitor's browser

    App Server
Acts as an Intermediary between browser-based DataBases and Backend DataBases and Legacy systems.
In many uses, the App server combines with HTTP to form the Web-App-Server

    Role of the DataBase
Organizes the information collected to make it easily accessible, managable and updatable with minimal issues

    Issues
    SPOF(Single Point of Failure)
If component of a system fails, there is no backup that can support the system's functionality bringing the
whole system to a collpase

    Downtime and Maintenance issues
When the system of a structure(node) needs to be repaired, the system has to be shut down while the maintenance is down, meaning that a client cannot be able to make a successful request.

    Traffic Overload
There is no possibility to scale the service with additional servers as backup.This leads to possible breakdown.
