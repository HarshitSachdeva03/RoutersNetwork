# RoutersNetwork
 Let n denote the number of routers in our network, and let’s say that the routers are labeled 0,...,n − 1.
 Each link is specified by a tuple (u,v,c), where u and v are the endpoints of the link and c is its capacity.
 Such a link is able to transfer a packet of size at most c from u to v and from v to u (every link is bidirectional
 and has the same capacity in either direction). Given the identities s and t of the source and the target router
 respectively, this project aims to determine the largest C such that a packet of size C can be transferred over the
 network from s to t. I have written a program to find that C and a sequence of routers v0,v1,...,vr−1,
 where s = v0 and v(r−1) = t, such that for each i, there exists a link of capacity at least C between v(i−1) and
 vi.
