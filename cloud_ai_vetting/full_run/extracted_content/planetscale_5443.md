# PlanetScale
**URL:** https://planetscale.com
**Page Title:** PlanetScale - the world’s fastest and most scalable cloud hosting for Vitess and Postgres
--------------------


## The world’s fastest and most scalable cloud databases

PlanetScale brings you the fastest databases available in the cloud. Both our Postgres and Vitess databases deliver exceptional speed and reliability, with Vitess adding ultra scalability through horizontal sharding.
Our blazing fast NVMe drives unlock unlimited IOPS , bringing data center performance to the cloud. We offer a range of deployment options to cover all of your security and compliance requirements — including bring your own cloud with PlanetScale Managed .
[LINK: deployment options](/docs/plans/deployment-options)
[LINK: PlanetScale Managed](/docs/vitess/managed)
PlanetScale powers Tier 0 databases at:
– Sualeh Asif - Chief Product Officer @Anysphere (Cursor)
Vitess allows MySQL databases to scale horizontally through explicit sharding — enabling a shared nothing architecture distributing data across thousands of nodes, all routed through a single database connection.
[LINK: scale horizontally through explicit sharding](/docs/vitess/sharding/sharding-quickstart)
Vitess was developed at YouTube by the founders of PlanetScale to scale their main MySQL database to petabytes of data on 70,000 nodes across 20 data centers. Now maintained and managed by PlanetScale, Vitess powers the databases of some of the web's largest properties: Slack, HubSpot, Blizzard, Etsy, GitHub, Block, Bloomberg, Yelp, and more.
– Ryan Sherlock @Intercom
PlanetScale Postgres starts at $5 per month and gives you a fully managed PostgreSQL cluster built for performance and reliability, offering first-class tooling without sacrificing developer experience. Available in AWS and GCP. High availability clusters deliver automatic failover across three availability zones.
[LINK: PlanetScale Postgres](/docs/postgres)
PlanetScale Metal starts at $50 per month for NVMe-backed performance with unlimited IOPS .
- PlanetScale Metal is benchmarked as the fastest Postgres in the cloud
- High availability: 1 primary and 2 replicas across three AZs with automated failover.
- Connection pooling with PgBouncer (port 6432 ) and buffered failovers to minimize impact.
- Branch-per-environment; each branch runs on its own dedicated cluster, priced prorated to the millisecond.
- Scale reads with replicas , streamline schema work with branching , and protect data with automated backups .
[LINK: replicas](/docs/postgres/scaling/replicas)
[LINK: branching](/docs/postgres/branching)
[LINK: automated backups](/docs/postgres/backups)
Get started with the Postgres quickstart or read the Postgres documentation .
[LINK: Postgres quickstart](/docs/postgres/tutorials/planetscale-postgres-quickstart)
[LINK: Postgres documentation](/docs/postgres)
Neki is our next-generation Postgres sharding architecture inspired by everything we have learned building Vitess: a fresh design from first principles to bring massive scale and reliability to PostgreSQL workloads. Follow progress on our blog and join the waitlist.
- Built for large scale Postgres workloads.
- Designed for predictable performance and fault tolerance at scale.
- Learn more in Announcing Neki and the PlanetScale for Postgres announcement .
Interested in early access? Visit neki.dev .

## Performance

PlanetScale Metal allows you to run your database on the fastest servers available in the cloud. Our blazing fast NVMe drives unlock unlimited IOPS and drastically lower latencies compared to other cloud database providers like Amazon Aurora and GCP Cloud SQL.
– Aaron Young @ Cash App

## Uptime

Ensuring your database is always running and your data is always safe is our number one priority. Nothing comes before uptime and reliability. Our SLA commitment is 99.999% for multi-region deployments and 99.99% for single-region deployments.
PlanetScale’s platform far exceeds the reliability of database services like Amazon Aurora/RDS and Google Cloud SQL with superior architecture and by making all database operations online.
- Deploy schema changes fully online
[LINK: Deploy schema changes fully online](/docs/vitess/schema-changes)
- Revertable schema changes (with zero data loss)
[LINK: Revertable schema changes (with zero data loss)](/docs/vitess/schema-changes/deploy-requests#revert-a-schema-change)
- Directing traffic to new read-only replicas
- Online MySQL and Vitess version updates
- Online cluster resizing and resharding
[LINK: Online cluster resizing and resharding](/docs/plans/cluster-sizing#upsizing-and-downsizing-clusters)
You can check out our track record on our status page .
– Todd Berman @Attentive

## Cost

At PlanetScale we believe cost is a unit of scale. Our product is less expensive than RDS MySQL and Aurora for around 85% of the workloads that customers have migrated to Metal. Getting a custom quote is easy: reach out to us . No long sales process or annoying pitches — you can probably tell from our website that the tech speaks for itself.
- No matter the size of your workload, PlanetScale Metal has the best price to performance ratio of any database service.
- Bring your own cloud with PlanetScale Managed
[LINK: PlanetScale Managed](/docs/vitess/managed)
- Purchase through the AWS Marketplace or the GCP Marketplace
- Customers running Metal on PlanetScale Managed can realize additional savings through Reserved Instances or Savings Plans — discounts otherwise not available on traditional EBS volumes.

## Security

PlanetScale is trusted by some of the world’s largest brands. Our core infrastructure was built to comply with high standards of security, compliance, and privacy.
- SOC 1 Type 2 & SOC 2 Type 2+ HIPAA compliance
- PCI DSS 4.0 compliance as a Level 1 Service Provider
- HIPAA Business Associate Agreements available on all plans
Learn more about our security and compliance practices in the security documentation .
[LINK: security documentation](/docs/security)
– Aaron Young @Cash App
Visit our Trust Center to request the latest copy of our SOC reports, PCI DSS Attestation of Compliance, and more.

## Features

PlanetScale is an opinionated database platform built by the infrastructure teams behind Facebook, GitHub, Twitter, Slack, YouTube, and more . All of our features combine to provide an end-to-end database management platform that prevents human error and provides full insight into query performance with actionable recommendations to make your database faster.
- Branching and deploy requests for zero downtime schema changes that your team can review.
- Store your vector data alongside your application’s relational MySQL data with PlanetScale vector support.
[LINK: vector data](/docs/vitess/vectors)
- Roll back bad schema changes with no downtime and no data loss.
- Full database observability with Insights to give you a detailed overview of cluster health.
[LINK: with Insights](/docs/vitess/monitoring/query-insights)
- Automate the horizontal scaling of your database with our explicit sharding workflows .
[LINK: explicit sharding workflows](/docs/vitess/sharding/sharding-quickstart)
- Utilize our Global Edge Network to automatically route query traffic to local nodes.
- Integrations with Fivetran, Airbyte, Hightouch, Datadog, Vantage, Debezium, and more .
[LINK: and more](/docs/vitess/etl)
- All of this is backed by our best-in-class support .
[LINK: best-in-class support](/docs/support)
– Chris Karper @ MyFitnessPal

--------------------