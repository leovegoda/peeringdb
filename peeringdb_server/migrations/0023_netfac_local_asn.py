# Generated by Django 1.11.23 on 2019-12-10 12:55

from django.db import migrations
from django.db.models import Count
from django.db.utils import IntegrityError


def forwards_func(apps, schema_editor):
    """
    since `local_asn` will no longer be included as part of the
    unique key for netfac we need to remove any potential dupes
    that may exist because of that

    We do this by setting the related network to be the network that
    matches the local_asn value
    """

    NetworkFacility = apps.get_model("peeringdb_server", "NetworkFacility")
    Network = apps.get_model("peeringdb_server", "Network")

    removed_dupe = 0
    asn_missing = 0
    migrated = 0

    print("\nmigrating netfacs")

    for netfac in NetworkFacility.handleref.all():
        if netfac.local_asn != netfac.network.asn:
            # local_asn differs from related network asn

            # next check if the network facility we are about
            # to migrate already exists, if it does, skip it

            qset = NetworkFacility.handleref.filter(
                network__asn=netfac.local_asn,
                facility_id=netfac.facility_id,
                local_asn=netfac.local_asn,
            )

            if qset.exists():
                notes = "Removed duplicate netfac for AS{} @ fac{}".format(
                    netfac.local_asn, netfac.facility_id
                )
                netfac.notes = notes
                netfac.status = "deleted"
                netfac.local_asn = None
                netfac.save()
                removed_dupe += 1
                continue

            net = Network.handleref.filter(asn=netfac.local_asn).first()

            if net and netfac.status == "ok":
                # set network object from local_asn

                if net.status != netfac.status:
                    # network status doesnt match netfac status
                    # we update netfac status to match as that is the least
                    # destructive behaviour while allowing us to still
                    # resolve the unique constraint conflict

                    netfac.status = net.status

                    print(
                        "AS{}: netfac{} at facility {} has been moved to network AS{}, however status"
                        " between the two was mismatching and has been corrected, "
                        "but should be reviewed".format(
                            netfac.network.asn, netfac.facility.id, netfac.id, net.asn
                        )
                    )

                netfac.network = net
                netfac.save()
                migrated += 1

            else:
                # could not find network with asn matching local_asn
                # in this case we should drop the netfac and log it

                notes = "AS{}: Could not correct non-existant local_asn AS{} @ fac{} ".format(
                    netfac.network.asn, netfac.local_asn, netfac.facility.id
                )
                if netfac.status == "ok":
                    print(notes)
                    asn_missing += 1

                continue

    print(f"Changed related network for {migrated} netfacs")
    print(
        "Deleted {} netfacs for being dupes after removal of local_asn".format(
            removed_dupe
        )
    )
    print(
        "Found {} netfacs where network matching local_asn did not exist".format(
            asn_missing
        )
    )


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0022_ixlan_remove_auto_increment"),
    ]

    operations = [
        migrations.RunPython(forwards_func, migrations.RunPython.noop),
    ]
