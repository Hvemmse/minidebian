# minidebian
minidebian


Installation på Dansk

**Trin 1: Forberedelse:**

1. **Download Debian netboot mini.iso:** Gå til Debian's officielle netboot-siden: [https://www.debian.org/distrib/netinst#netboot](https://www.debian.org/distrib/netinst#netboot). Vælg din arkitektur (normalt amd64 for moderne computere), og download netboot mini.iso-filen.

**Trin 2: Opret en harddisk image:**

1. **Opret en 8 GB harddisk image:** Åbn en terminal på din computer og naviger til en mappe, hvor du vil gemme harddisk image-filen. Kør følgende kommando for at oprette en 8 GB harddisk image:
   
   ```bash
   qemu-img create debian.img 8G
   ```

2. **Installer QEMU:** Hvis du ikke allerede har QEMU installeret, kan du installere det ved at køre følgende kommando (kommandoen kan variere afhængigt af dit system):
   
   ```bash
   sudo apt-get install qemu-system-x86
   ```

**Trin 3: Start QEMU med netboot mini.iso:**

1. **Start QEMU:** Kør følgende kommando for at starte QEMU med den oprettede harddisk image og Debian netboot mini.iso:

   ```bash
   qemu-system-x86_64 -hda debian.img -boot d -cdrom mini.iso -m 1024
   ```

   Dette starter en virtuel maskine med 1 GB RAM og booter fra netboot mini.iso.

2. **Installér Debian:** Følg installationsprocessen, som du gjorde før i den tidligere vejledning. Vælg dine indstillinger, og når du når til partitionering, skal du vælge "Guided - use entire disk" og derefter vælge din virtuelle harddisk (normalt `/dev/sda`).

3. **Afslut installationen:** Gennemfør installationsprocessen og fjern netboot mini.iso, når det bliver bedt om. Genstart derefter den virtuelle maskine.

**Trin 4: Brug din virtuelle Debian-installation:**

1. **Start den virtuelle maskine:** Naviger til mappen, hvor du oprettede harddisk image-filen, og kør kommandoen:

   ```bash
   qemu-system-x86_64 -hda debian.img -m 1024
   ```

   Dette starter din virtuelle Debian-installation.

2. **Log ind:** Når den virtuelle maskine starter, bliver du bedt om at logge ind med den bruger og adgangskode, du oprettede under installationen.

3. **Brug Debian:** Nu kan du bruge din virtuelle Debian-installation ligesom en almindelig Debian-installation.

Husk, at QEMU-kommandoerne kan variere afhængigt af dit system og præferencer. Juster kommandoerne, hvis nødvendigt, og sørg for at have tilstrækkelig teknisk viden om din computer og virtuelle maskiner, inden du begynder.
