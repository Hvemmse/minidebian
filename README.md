# minidebian
minidebian

# Installation in English


**Step 1: Preparation:**

1. **Download Debian netboot mini.iso:** Go to Debian's official netboot page: [https://www.debian.org/distrib/netinst#netboot](https://www.debian.org/distrib/netinst#netboot). Choose your architecture (usually amd64 for modern computers), and download the netboot mini.iso file.

**Step 2: Create a Hard Disk Image:**

1. **Create an 8 GB hard disk image:** Open a terminal on your computer and navigate to a directory where you want to save the hard disk image file. Run the following command to create an 8 GB hard disk image:

   ```bash
   qemu-img create debian.img 8G
   ```

2. **Install QEMU:** If you don't already have QEMU installed, you can install it by running the following command (the command might vary depending on your system):

   ```bash
   sudo apt-get install qemu-system-x86
   ```

**Step 3: Start QEMU with netboot mini.iso:**

1. **Start QEMU:** Run the following command to start QEMU with the created hard disk image and Debian netboot mini.iso:

   ```bash
   qemu-system-x86_64 -hda debian.img -boot d -cdrom mini.iso -m 1024
   ```

   This will start a virtual machine with 1 GB of RAM and boot from the netboot mini.iso.

2. **Install Debian:** Follow the installation process as you did before in the previous guide. Choose your settings, and when you reach the partitioning step, select "Guided - use entire disk" and then choose your virtual hard disk (usually `/dev/sda`).

3. **Finish Installation:** Complete the installation process and remove the netboot mini.iso when prompted. Then restart the virtual machine.

**Step 4: Use Your Virtual Debian Installation:**

1. **Start the Virtual Machine:** Navigate to the directory where you created the hard disk image file and run the command:

   ```bash
   qemu-system-x86_64 -hda debian.img -m 1024
   ```

   This will start your virtual Debian installation.

2. **Log In:** When the virtual machine starts, you'll be prompted to log in with the user and password you created during the installation.

3. **Use Debian:** Now you can use your virtual Debian installation just like a regular Debian installation.

Remember that QEMU commands can vary depending on your system and preferences. Adjust the commands if necessary, and make sure you have sufficient technical knowledge about your computer and virtual machines before you begin.

# Installation på Dansk

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
