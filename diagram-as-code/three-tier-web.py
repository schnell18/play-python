#!/usr/bin/env python3

from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.network import ELB, Route53

if __name__ == "__main__":
    with Diagram("Example AWS Architecture", show=False):
        dns = Route53("dns")
        lb = ELB("lb")

        with Cluster("Services"):
            svc_group = [
                ECS("web1"),
                ECS("web2"),
                ECS("web3"),
            ]

        with Cluster("DB Cluster"):
            db_primary = RDS("userdb")
            db_primary - RDS("userdb ro")

        memcached = ElastiCache("memcached")

        dns >> lb >> svc_group
        svc_group >> db_primary
        svc_group >> memcached
