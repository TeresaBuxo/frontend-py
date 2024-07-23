import reflex as rx

class SelectorsState(rx.State):
    verified: str = "All"
    type_site: str = "All"
    type_medical_equipment: str = "All"


def select(label, items, value, on_change):
    return rx.flex(
        rx.text(label),
        rx.select.root(
            rx.select.trigger(),
            rx.select.content(
                *[
                    rx.select.item(item, value=item)
                    for item in items
                ]
            ),
            value=value,
            on_change=on_change,
        ),
        align="center",
        justify="center",
        direction="column",
    )


def selectors():
    return rx.flex(
        select(
            "Verified sites",
            ["All", "Verified", "Non-verifies"],
            SelectorsState.verified,
            SelectorsState.set_verified,
        ),
        select(
            "Type of site",
            [
                "All",
                "ONG intermediate",
                "Builder/Manufacturer",
                "Designer",
                "Hospital/Clinic",
                "Maintainer",
                "Trasnportation",
            ],
            SelectorsState.type_site,
            SelectorsState.set_type_site,
        ),
        select(
            "Type of Medical Equipment",
            [
                "All",
                "Incubator",
                "Respirator",
                "CPAP",
                "Wheelchair",
            ],
            SelectorsState.type_medical_equipment,
            SelectorsState.set_type_medical_equipment,
        ),
        width="100%",
        spacing="2",
        justify="between",
    )
