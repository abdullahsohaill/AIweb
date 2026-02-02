# here.
**URL:** https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.17.4
**Page Title:** 
--------------------

### (Raw Extraction Fallback)

commit 6c7871823908a4330e145d635371582f76ce1407
Author: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Date:   Sun Oct 19 16:37:45 2025 +0200

    Linux 6.17.4
    
    Link: https://lore.kernel.org/r/20251017145201.780251198@linuxfoundation.org
    Tested-by: Ronald Warsow <rwarsow@gmx.de>
    Tested-by: Jon Hunter <jonathanh@nvidia.com>
    Tested-by: Hardik Garg <hargar@linux.microsoft.com>
    Tested-by: Salvatore Bonaccorso <carnil@debian.org>
    Tested-by: Shuah Khan <skhan@linuxfoundation.org>
    Tested-by: Florian Fainelli <florian.fainelli@broadcom.com>
    Tested-by: Peter Schneider <pschneider1968@googlemail.com>
    Tested-by: Brett A C Sheffield <bacs@librecast.net>
    Tested-by: Dileep Malepu <dileep.debian@gmail.com>
    Tested-by: Markus Reichelt <lkt+2023@mareichelt.com>
    Tested-by: Miguel Ojeda <ojeda@kernel.org>
    Tested-by: Pascal Ernster <git@hardfalcon.net>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 99ae3e70a293834d0274c46a37120c71a24a4995
Author: Christian Brauner <brauner@kernel.org>
Date:   Mon Sep 29 11:41:16 2025 +0200

    mount: handle NULL values in mnt_ns_release()
    
    [ Upstream commit 6c7ca6a02f8f9549a438a08a23c6327580ecf3d6 ]
    
    When calling in listmount() mnt_ns_release() may be passed a NULL
    pointer. Handle that case gracefully.
    
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit bf0fbf5e8b0aff8a4a0fb35e32b10083baa83c04
Author: Christian Brauner <brauner@kernel.org>
Date:   Fri Sep 12 13:52:24 2025 +0200

    pidfs: validate extensible ioctls
    
    [ Upstream commit 3c17001b21b9f168c957ced9384abe969019b609 ]
    
    Validate extensible ioctls stricter than we do now.
    
    Reviewed-by: Aleksa Sarai <cyphar@cyphar.com>
    Reviewed-by: Jan Kara <jack@suse.cz>
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 9f0f659ea927a5c3cf655338ad6c37dc257f3460
Author: Darrick J. Wong <djwong@kernel.org>
Date:   Tue Sep 16 08:00:45 2025 -0700

    iomap: error out on file IO when there is no inline_data buffer
    
    [ Upstream commit 6a96fb653b6481ec73e9627ade216b299e4de9ea ]
    
    Return IO errors if an ->iomap_begin implementation returns an
    IOMAP_INLINE buffer but forgets to set the inline_data pointer.
    Filesystems should never do this, but we could help fs developers (me)
    fix their bugs by handling this more gracefully than crashing the
    kernel.
    
    Signed-off-by: Darrick J. Wong <djwong@kernel.org>
    Link: https://lore.kernel.org/175803480324.966383.7414345025943296442.stgit@frogsfrogsfrogs
    Reviewed-by: Christoph Hellwig <hch@lst.de>
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 8167718b599e341d8bdc34e3ee4283fc6a97c1a8
Author: Jan Kara <jack@suse.cz>
Date:   Fri Sep 12 12:38:37 2025 +0200

    writeback: Avoid excessively long inode switching times
    
    [ Upstream commit 9a6ebbdbd41235ea3bc0c4f39e2076599b8113cc ]
    
    With lazytime mount option enabled we can be switching many dirty inodes
    on cgroup exit to the parent cgroup. The numbers observed in practice
    when systemd slice of a large cron job exits can easily reach hundreds
    of thousands or millions. The logic in inode_do_switch_wbs() which sorts
    the inode into appropriate place in b_dirty list of the target wb
    however has linear complexity in the number of dirty inodes thus overall
    time complexity of switching all the inodes is quadratic leading to
    workers being pegged for hours consuming 100% of the CPU and switching
    inodes to the parent wb.
    
    Simple reproducer of the issue:
      FILES=10000
      # Filesystem mounted with lazytime mount option
      MNT=/mnt/
      echo "Creating files and switching timestamps"
      for (( j = 0; j < 50; j ++ )); do
          mkdir $MNT/dir$j
          for (( i = 0; i < $FILES; i++ )); do
              echo "foo" >$MNT/dir$j/file$i
          done
          touch -a -t 202501010000 $MNT/dir$j/file*
      done
      wait
      echo "Syncing and flushing"
      sync
      echo 3 >/proc/sys/vm/drop_caches
    
      echo "Reading all files from a cgroup"
      mkdir /sys/fs/cgroup/unified/mycg1 || exit
      echo $$ >/sys/fs/cgroup/unified/mycg1/cgroup.procs || exit
      for (( j = 0; j < 50; j ++ )); do
          cat /mnt/dir$j/file* >/dev/null &
      done
      wait
      echo "Switching wbs"
      # Now rmdir the cgroup after the script exits
    
    We need to maintain b_dirty list ordering to keep writeback happy so
    instead of sorting inode into appropriate place just append it at the
    end of the list and clobber dirtied_time_when. This may result in inode
    writeback starting later after cgroup switch however cgroup switches are
    rare so it shouldn't matter much. Since the cgroup had write access to
    the inode, there are no practical concerns of the possible DoS issues.
    
    Acked-by: Tejun Heo <tj@kernel.org>
    Signed-off-by: Jan Kara <jack@suse.cz>
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 6d3563a6bfa62ae14df2248e813481f1c948b0b3
Author: Jan Kara <jack@suse.cz>
Date:   Fri Sep 12 12:38:36 2025 +0200

    writeback: Avoid softlockup when switching many inodes
    
    [ Upstream commit 66c14dccd810d42ec5c73bb8a9177489dfd62278 ]
    
    process_inode_switch_wbs_work() can be switching over 100 inodes to a
    different cgroup. Since switching an inode requires counting all dirty &
    under-writeback pages in the address space of each inode, this can take
    a significant amount of time. Add a possibility to reschedule after
    processing each inode to avoid softlockups.
    
    Acked-by: Tejun Heo <tj@kernel.org>
    Signed-off-by: Jan Kara <jack@suse.cz>
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 7381cd12252565a83f5060ee7e9bf3aa40e9265a
Author: Al Viro <viro@zeniv.linux.org.uk>
Date:   Tue Aug 26 16:35:55 2025 -0400

    mnt_ns_tree_remove(): DTRT if mnt_ns had never been added to mnt_ns_list
    
    [ Upstream commit 38f4885088fc5ad41b8b0a2a2cfc73d01e709e5c ]
    
    Actual removal is done under the lock, but for checking if need to bother
    the lockless RB_EMPTY_NODE() is safe - either that namespace had never
    been added to mnt_ns_tree, in which case the the node will stay empty, or
    whoever had allocated it has called mnt_ns_tree_add() and it has already
    run to completion.  After that point RB_EMPTY_NODE() will become false and
    will remain false, no matter what we do with other nodes in the tree.
    
    Reviewed-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Al Viro <viro@zeniv.linux.org.uk>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit b7b12f5e02e30f015888ce86cad88a8a62e61534
Author: Christian Brauner <brauner@kernel.org>
Date:   Fri Sep 12 13:52:26 2025 +0200

    nsfs: validate extensible ioctls
    
    [ Upstream commit f8527a29f4619f74bc30a9845ea87abb9a6faa1e ]
    
    Validate extensible ioctls stricter than we do now.
    
    Reviewed-by: Jan Kara <jack@suse.cz>
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 5211c672ea2490a11ea6a158d5d6a7a05a9c15d3
Author: Tetsuo Handa <penguin-kernel@I-love.SAKURA.ne.jp>
Date:   Sat Aug 30 19:01:01 2025 +0900

    cramfs: Verify inode mode when loading from disk
    
    [ Upstream commit 7f9d34b0a7cb93d678ee7207f0634dbf79e47fe5 ]
    
    The inode mode loaded from corrupted disk can be invalid. Do like what
    commit 0a9e74051313 ("isofs: Verify inode mode when loading from disk")
    does.
    
    Reported-by: syzbot <syzbot+895c23f6917da440ed0d@syzkaller.appspotmail.com>
    Closes: https://syzkaller.appspot.com/bug?extid=895c23f6917da440ed0d
    Signed-off-by: Tetsuo Handa <penguin-kernel@I-love.SAKURA.ne.jp>
    Link: https://lore.kernel.org/429b3ef1-13de-4310-9a8e-c2dc9a36234a@I-love.SAKURA.ne.jp
    Acked-by: Nicolas Pitre <nico@fluxnic.net>
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 3b72a03bf5fe3b2cc1a7b9ca3d4a47f73d1189d1
Author: Lichen Liu <lichliu@redhat.com>
Date:   Fri Aug 15 20:14:59 2025 +0800

    fs: Add 'initramfs_options' to set initramfs mount options
    
    [ Upstream commit 278033a225e13ec21900f0a92b8351658f5377f2 ]
    
    When CONFIG_TMPFS is enabled, the initial root filesystem is a tmpfs.
    By default, a tmpfs mount is limited to using 50% of the available RAM
    for its content. This can be problematic in memory-constrained
    environments, particularly during a kdump capture.
    
    In a kdump scenario, the capture kernel boots with a limited amount of
    memory specified by the 'crashkernel' parameter. If the initramfs is
    large, it may fail to unpack into the tmpfs rootfs due to insufficient
    space. This is because to get X MB of usable space in tmpfs, 2*X MB of
    memory must be available for the mount. This leads to an OOM failure
    during the early boot process, preventing a successful crash dump.
    
    This patch introduces a new kernel command-line parameter,
    initramfs_options, which allows passing specific mount options directly
    to the rootfs when it is first mounted. This gives users control over
    the rootfs behavior.
    
    For example, a user can now specify initramfs_options=size=75% to allow
    the tmpfs to use up to 75% of the available memory. This can
    significantly reduce the memory pressure for kdump.
    
    Consider a practical example:
    
    To unpack a 48MB initramfs, the tmpfs needs 48MB of usable space. With
    the default 50% limit, this requires a memory pool of 96MB to be
    available for the tmpfs mount. The total memory requirement is therefore
    approximately: 16MB (vmlinuz) + 48MB (loaded initramfs) + 48MB (unpacked
    kernel) + 96MB (for tmpfs) + 12MB (runtime overhead) ≈ 220MB.
    
    By using initramfs_options=size=75%, the memory pool required for the
    48MB tmpfs is reduced to 48MB / 0.75 = 64MB. This reduces the total
    memory requirement by 32MB (96MB - 64MB), allowing the kdump to succeed
    with a smaller crashkernel size, such as 192MB.
    
    An alternative approach of reusing the existing rootflags parameter was
    considered. However, a new, dedicated initramfs_options parameter was
    chosen to avoid altering the current behavior of rootflags (which
    applies to the final root filesystem) and to prevent any potential
    regressions.
    
    Also add documentation for the new kernel parameter "initramfs_options"
    
    This approach is inspired by prior discussions and patches on the topic.
    Ref: https://www.lightofdawn.org/blog/?viewDetailed=00128
    Ref: https://landley.net/notes-2015.html#01-01-2015
    Ref: https://lkml.org/lkml/2021/6/29/783
    Ref: https://www.kernel.org/doc/html/latest/filesystems/ramfs-rootfs-initramfs.html#what-is-rootfs
    
    Signed-off-by: Lichen Liu <lichliu@redhat.com>
    Link: https://lore.kernel.org/20250815121459.3391223-1-lichliu@redhat.com
    Tested-by: Rob Landley <rob@landley.net>
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit a0212978af1825b37da0b453b94d9b0e5af11478
Author: gaoxiang17 <gaoxiang17@xiaomi.com>
Date:   Sat Aug 2 10:21:23 2025 +0800

    pid: Add a judgment for ns null in pid_nr_ns
    
    [ Upstream commit 006568ab4c5ca2309ceb36fa553e390b4aa9c0c7 ]
    
    __task_pid_nr_ns
            ns = task_active_pid_ns(current);
            pid_nr_ns(rcu_dereference(*task_pid_ptr(task, type)), ns);
                    if (pid && ns->level <= pid->level) {
    
    Sometimes null is returned for task_active_pid_ns. Then it will trigger kernel panic in pid_nr_ns.
    
    For example:
            Unable to handle kernel NULL pointer dereference at virtual address 0000000000000058
            Mem abort info:
            ESR = 0x0000000096000007
            EC = 0x25: DABT (current EL), IL = 32 bits
            SET = 0, FnV = 0
            EA = 0, S1PTW = 0
            FSC = 0x07: level 3 translation fault
            Data abort info:
            ISV = 0, ISS = 0x00000007, ISS2 = 0x00000000
            CM = 0, WnR = 0, TnD = 0, TagAccess = 0
            GCS = 0, Overlay = 0, DirtyBit = 0, Xs = 0
            user pgtable: 4k pages, 39-bit VAs, pgdp=00000002175aa000
            [0000000000000058] pgd=08000002175ab003, p4d=08000002175ab003, pud=08000002175ab003, pmd=08000002175be003, pte=0000000000000000
            pstate: 834000c5 (Nzcv daIF +PAN -UAO +TCO +DIT -SSBS BTYPE=--)
            pc : __task_pid_nr_ns+0x74/0xd0
            lr : __task_pid_nr_ns+0x24/0xd0
            sp : ffffffc08001bd10
            x29: ffffffc08001bd10 x28: ffffffd4422b2000 x27: 0000000000000001
            x26: ffffffd442821168 x25: ffffffd442821000 x24: 00000f89492eab31
            x23: 00000000000000c0 x22: ffffff806f5693c0 x21: ffffff806f5693c0
            x20: 0000000000000001 x19: 0000000000000000 x18: 0000000000000000
            x17: 00000000529c6ef0 x16: 00000000529c6ef0 x15: 00000000023a1adc
            x14: 0000000000000003 x13: 00000000007ef6d8 x12: 001167c391c78800
            x11: 00ffffffffffffff x10: 0000000000000000 x9 : 0000000000000001
            x8 : ffffff80816fa3c0 x7 : 0000000000000000 x6 : 49534d702d535449
            x5 : ffffffc080c4c2c0 x4 : ffffffd43ee128c8 x3 : ffffffd43ee124dc
            x2 : 0000000000000000 x1 : 0000000000000001 x0 : ffffff806f5693c0
            Call trace:
            __task_pid_nr_ns+0x74/0xd0
            ...
            __handle_irq_event_percpu+0xd4/0x284
            handle_irq_event+0x48/0xb0
            handle_fasteoi_irq+0x160/0x2d8
            generic_handle_domain_irq+0x44/0x60
            gic_handle_irq+0x4c/0x114
            call_on_irq_stack+0x3c/0x74
            do_interrupt_handler+0x4c/0x84
            el1_interrupt+0x34/0x58
            el1h_64_irq_handler+0x18/0x24
            el1h_64_irq+0x68/0x6c
            account_kernel_stack+0x60/0x144
            exit_task_stack_account+0x1c/0x80
            do_exit+0x7e4/0xaf8
            ...
            get_signal+0x7bc/0x8d8
            do_notify_resume+0x128/0x828
            el0_svc+0x6c/0x70
            el0t_64_sync_handler+0x68/0xbc
            el0t_64_sync+0x1a8/0x1ac
            Code: 35fffe54 911a02a8 f9400108 b4000128 (b9405a69)
            ---[ end trace 0000000000000000 ]---
            Kernel panic - not syncing: Oops: Fatal exception in interrupt
    
    Signed-off-by: gaoxiang17 <gaoxiang17@xiaomi.com>
    Link: https://lore.kernel.org/20250802022123.3536934-1-gxxa03070307@gmail.com
    Reviewed-by: Baoquan He <bhe@redhat.com>
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 23f12d18de41841225281129a2f6308e773c34d4
Author: Tetsuo Handa <penguin-kernel@I-love.SAKURA.ne.jp>
Date:   Wed Aug 13 00:17:44 2025 +0900

    minixfs: Verify inode mode when loading from disk
    
    [ Upstream commit 73861970938ad1323eb02bbbc87f6fbd1e5bacca ]
    
    The inode mode loaded from corrupted disk can be invalid. Do like what
    commit 0a9e74051313 ("isofs: Verify inode mode when loading from disk")
    does.
    
    Reported-by: syzbot <syzbot+895c23f6917da440ed0d@syzkaller.appspotmail.com>
    Closes: https://syzkaller.appspot.com/bug?extid=895c23f6917da440ed0d
    Signed-off-by: Tetsuo Handa <penguin-kernel@I-love.SAKURA.ne.jp>
    Link: https://lore.kernel.org/ec982681-84b8-4624-94fa-8af15b77cbd2@I-love.SAKURA.ne.jp
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 03dec283fc528dcb8df3190493ad334829592e9c
Author: Miklos Szeredi <mszeredi@redhat.com>
Date:   Wed Aug 13 17:11:05 2025 +0200

    copy_file_range: limit size if in compat mode
    
    [ Upstream commit f8f59a2c05dc16d19432e3154a9ac7bc385f4b92 ]
    
    If the process runs in 32-bit compat mode, copy_file_range results can be
    in the in-band error range.  In this case limit copy length to MAX_RW_COUNT
    to prevent a signed overflow.
    
    Reported-by: Florian Weimer <fweimer@redhat.com>
    Closes: https://lore.kernel.org/all/lhuh5ynl8z5.fsf@oldenburg.str.redhat.com/
    Signed-off-by: Miklos Szeredi <mszeredi@redhat.com>
    Link: https://lore.kernel.org/20250813151107.99856-1-mszeredi@redhat.com
    Reviewed-by: Amir Goldstein <amir73il@gmail.com>
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 9d0ac18eb59f7d5d6f660385f827663dd252fd62
Author: Lucas Zampieri <lzampier@redhat.com>
Date:   Tue Sep 23 15:43:19 2025 +0100

    irqchip/sifive-plic: Avoid interrupt ID 0 handling during suspend/resume
    
    [ Upstream commit f75e07bf5226da640fa99a0594687c780d9bace4 ]
    
    According to the PLIC specification[1], global interrupt sources are
    assigned small unsigned integer identifiers beginning at the value 1.
    An interrupt ID of 0 is reserved to mean "no interrupt".
    
    The current plic_irq_resume() and plic_irq_suspend() functions incorrectly
    start the loop from index 0, which accesses the register space for the
    reserved interrupt ID 0.
    
    Change the loop to start from index 1, skipping the reserved
    interrupt ID 0 as per the PLIC specification.
    
    This prevents potential undefined behavior when accessing the reserved
    register space during suspend/resume cycles.
    
    Fixes: e80f0b6a2cf3 ("irqchip/irq-sifive-plic: Add syscore callbacks for hibernation")
    Co-developed-by: Jia Wang <wangjia@ultrarisc.com>
    Signed-off-by: Jia Wang <wangjia@ultrarisc.com>
    Co-developed-by: Charles Mirabile <cmirabil@redhat.com>
    Signed-off-by: Charles Mirabile <cmirabil@redhat.com>
    Signed-off-by: Lucas Zampieri <lzampier@redhat.com>
    Signed-off-by: Thomas Gleixner <tglx@linutronix.de>
    Link: https://github.com/riscv/riscv-plic-spec/releases/tag/1.0.0
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 91f66152f502d81b83a0b7d7116ecad287aaf4cc
Author: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Date:   Thu Oct 16 12:04:43 2025 -0400

    ACPI: property: Do not pass NULL handles to acpi_attach_data()
    
    [ Upstream commit baf60d5cb8bc6b85511c5df5f0ad7620bb66d23c ]
    
    In certain circumstances, the ACPI handle of a data-only node may be
    NULL, in which case it does not make sense to attempt to attach that
    node to an ACPI namespace object, so update the code to avoid attempts
    to do so.
    
    This prevents confusing and unuseful error messages from being printed.
    
    Also document the fact that the ACPI handle of a data-only node may be
    NULL and when that happens in a code comment.  In addition, make
    acpi_add_nondev_subnodes() print a diagnostic message for each data-only
    node with an unknown ACPI namespace scope.
    
    Fixes: 1d52f10917a7 ("ACPI: property: Tie data nodes to acpi handles")
    Cc: 6.0+ <stable@vger.kernel.org> # 6.0+
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Reviewed-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Tested-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit e770b20cc99d606a328283843d60b35cdfd1703d
Author: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Date:   Thu Oct 16 12:04:42 2025 -0400

    ACPI: property: Add code comments explaining what is going on
    
    [ Upstream commit 737c3a09dcf69ba2814f3674947ccaec1861c985 ]
    
    In some places in the ACPI device properties handling code, it is
    unclear why the code is what it is.  Some assumptions are not documented
    and some pieces of code are based on knowledge that is not mentioned
    anywhere.
    
    Add code comments explaining these things.
    
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Reviewed-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Tested-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Stable-dep-of: baf60d5cb8bc ("ACPI: property: Do not pass NULL handles to acpi_attach_data()")
    Signed-off-by: Sasha Levin <sashal@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 716b9bc934fc591ece3a12a3ee8c8985a9d58e7d
Author: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Date:   Thu Oct 16 12:04:41 2025 -0400

    ACPI: property: Disregard references in data-only subnode lists
    
    [ Upstream commit d06118fe9b03426484980ed4c189a8c7b99fa631 ]
    
    Data-only subnode links following the ACPI data subnode GUID in a _DSD
    package are expected to point to named objects returning _DSD-equivalent
    packages.  If a reference to such an object is used in the target field
    of any of those links, that object will be evaluated in place (as a
    named object) and its return data will be embedded in the outer _DSD
    package.
    
    For this reason, it is not expected to see a subnode link with the
    target field containing a local reference (that would mean pointing
    to a device or another object that cannot be evaluated in place and
    therefore cannot return a _DSD-equivalent package).
    
    Accordingly, simplify the code parsing data-only subnode links to
    simply print a message when it encounters a local reference in the
    target field of one of those links.
    
    Moreover, since acpi_nondev_subnode_data_ok() would only have one
    caller after the change above, fold it into that caller.
    
    Link: https://lore.kernel.org/linux-acpi/CAJZ5v0jVeSrDO6hrZhKgRZrH=FpGD4vNUjFD8hV9WwN9TLHjzQ@mail.gmail.com/
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Reviewed-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Tested-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Stable-dep-of: baf60d5cb8bc ("ACPI: property: Do not pass NULL handles to acpi_attach_data()")
    Signed-off-by: Sasha Levin <sashal@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 3cae55fce2c5cd841134f40aeed70fa586aa5ed8
Author: Viken Dadhaniya <viken.dadhaniya@oss.qualcomm.com>
Date:   Thu Oct 16 15:38:01 2025 -0400

    arm64: dts: qcom: qcs615: add missing dt property in QUP SEs
    
    [ Upstream commit 6a5e9b9738a32229e2673d4eccfcbfe2ef3a1ab4 ]
    
    Add the missing required-opps and operating-points-v2 properties to
    several I2C, SPI, and UART nodes in the QUP SEs.
    
    Fixes: f6746dc9e379 ("arm64: dts: qcom: qcs615: Add QUPv3 configuration")
    Cc: stable@vger.kernel.org
    Signed-off-by: Viken Dadhaniya <viken.dadhaniya@oss.qualcomm.com>
    Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@oss.qualcomm.com>
    Link: https://lore.kernel.org/r/20250630064338.2487409-1-viken.dadhaniya@oss.qualcomm.com
    Signed-off-by: Bjorn Andersson <andersson@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit ac01416d477c2dc6016782635ae022f8cc634a29
Author: Edward Adam Davis <eadavis@qq.com>
Date:   Mon Oct 13 16:26:24 2025 -0400

    media: mc: Clear minor number before put device
    
    [ Upstream commit 8cfc8cec1b4da88a47c243a11f384baefd092a50 ]
    
    The device minor should not be cleared after the device is released.
    
    Fixes: 9e14868dc952 ("media: mc: Clear minor number reservation at unregistration time")
    Cc: stable@vger.kernel.org
    Reported-by: syzbot+031d0cfd7c362817963f@syzkaller.appspotmail.com
    Closes: https://syzkaller.appspot.com/bug?extid=031d0cfd7c362817963f
    Tested-by: syzbot+031d0cfd7c362817963f@syzkaller.appspotmail.com
    Signed-off-by: Edward Adam Davis <eadavis@qq.com>
    Signed-off-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    [ moved clear_bit from media_devnode_release callback to media_devnode_unregister before put_device ]
    Signed-off-by: Sasha Levin <sashal@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 3bd85ecc2253c20c25c246172165722060e395a2
Author: Donet Tom <donettom@linux.ibm.com>
Date:   Tue Oct 14 07:39:43 2025 -0400

    mm/ksm: fix incorrect KSM counter handling in mm_struct during fork
    
    [ Upstream commit 4d6fc29f36341d7795db1d1819b4c15fe9be7b23 ]
    
    Patch series "mm/ksm: Fix incorrect accounting of KSM counters during
    fork", v3.
    
    The first patch in this series fixes the incorrect accounting of KSM
    counters such as ksm_merging_pages, ksm_rmap_items, and the global
    ksm_zero_pages during fork.
    
    The following patch add a selftest to verify the ksm_merging_pages counter
    was updated correctly during fork.
    
    Test Results
    ============
    Without the first patch
    -----------------------
     # [RUN] test_fork_ksm_merging_page_count
     not ok 10 ksm_merging_page in child: 32
    
    With the first patch
    --------------------
     # [RUN] test_fork_ksm_merging_page_count
     ok 10 ksm_merging_pages is not inherited after fork
    
    This patch (of 2):
    
    Currently, the KSM-related counters in `mm_struct`, such as
    `ksm_merging_pages`, `ksm_rmap_items`, and `ksm_zero_pages`, are inherited
    by the child process during fork.  This results in inconsistent
    accounting.
    
    When a process uses KSM, identical pages are merged and an rmap item is
    created for each merged page.  The `ksm_merging_pages` and
    `ksm_rmap_items` counters are updated accordingly.  However, after a fork,
    these counters are copied to the child while the corresponding rmap items
    are not.  As a result, when the child later triggers an unmerge, there are
    no rmap items present in the child, so the counters remain stale, leading
    to incorrect accounting.
    
    A similar issue exists with `ksm_zero_pages`, which maintains both a
    global counter and a per-process counter.  During fork, the per-process
    counter is inherited by the child, but the global counter is not
    incremented.  Since the child also references zero pages, the global
    counter should be updated as well.  Otherwise, during zero-page unmerge,
    both the global and per-process counters are decremented, causing the
    global counter to become inconsistent.
    
    To fix this, ksm_merging_pages and ksm_rmap_items are reset to 0 during
    fork, and the global ksm_zero_pages counter is updated with the
    per-process ksm_zero_pages value inherited by the child.  This ensures
    that KSM statistics remain accurate and reflect the activity of each
    process correctly.
    
    Link: https://lkml.kernel.org/r/cover.1758648700.git.donettom@linux.ibm.com
    Link: https://lkml.kernel.org/r/7b9870eb67ccc0d79593940d9dbd4a0b39b5d396.1758648700.git.donettom@linux.ibm.com
    Fixes: 7609385337a4 ("ksm: count ksm merging pages for each process")
    Fixes: cb4df4cae4f2 ("ksm: count allocated ksm rmap_items for each process")
    Fixes: e2942062e01d ("ksm: count all zero pages placed by KSM")
    Signed-off-by: Donet Tom <donettom@linux.ibm.com>
    Reviewed-by: Chengming Zhou <chengming.zhou@linux.dev>
    Acked-by: David Hildenbrand <david@redhat.com>
    Cc: Aboorva Devarajan <aboorvad@linux.ibm.com>
    Cc: David Hildenbrand <david@redhat.com>
    Cc: Donet Tom <donettom@linux.ibm.com>
    Cc: "Ritesh Harjani (IBM)" <ritesh.list@gmail.com>
    Cc: Wei Yang <richard.weiyang@gmail.com>
    Cc: xu xin <xu.xin16@zte.com.cn>
    Cc: <stable@vger.kernel.org>    [6.6+]
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    [ replaced mm_flags_test() calls with test_bit() ]
    Signed-off-by: Sasha Levin <sashal@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f271155ff31aca8ef82c61c8df23ca97e9a77dd4
Author: Phillip Lougher <phillip@squashfs.org.uk>
Date:   Mon Oct 13 13:36:49 2025 -0400

    Squashfs: reject negative file sizes in squashfs_read_inode()
    
    [ Upstream commit 9f1c14c1de1bdde395f6cc893efa4f80a2ae3b2b ]
    
    Syskaller reports a "WARNING in ovl_copy_up_file" in overlayfs.
    
    This warning is ultimately caused because the underlying Squashfs file
    system returns a file with a negative file size.
    
    This commit checks for a negative file size and returns EINVAL.
    
    [phillip@squashfs.org.uk: only need to check 64 bit quantity]
      Link: https://lkml.kernel.org/r/20250926222305.110103-1-phillip@squashfs.org.uk
    Link: https://lkml.kernel.org/r/20250926215935.107233-1-phillip@squashfs.org.uk
    Fixes: 6545b246a2c8 ("Squashfs: inode operations")
    Signed-off-by: Phillip Lougher <phillip@squashfs.org.uk>
    Reported-by: syzbot+f754e01116421e9754b9@syzkaller.appspotmail.com
    Closes: https://lore.kernel.org/all/68d580e5.a00a0220.303701.0019.GAE@google.com/
    Cc: Amir Goldstein <amir73il@gmail.com>
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit c2188189bbed420feafe455ded2d2e225ae3cbea
Author: Phillip Lougher <phillip@squashfs.org.uk>
Date:   Mon Oct 13 13:36:48 2025 -0400

    Squashfs: add additional inode sanity checking
    
    [ Upstream commit 9ee94bfbe930a1b39df53fa2d7b31141b780eb5a ]
    
    Patch series "Squashfs: performance improvement and a sanity check".
    
    This patchset adds an additional sanity check when reading regular file
    inodes, and adds support for SEEK_DATA/SEEK_HOLE lseek() whence values.
    
    This patch (of 2):
    
    Add an additional sanity check when reading regular file inodes.
    
    A regular file if the file size is an exact multiple of the filesystem
    block size cannot have a fragment.  This is because by definition a
    fragment block stores tailends which are not a whole block in size.
    
    Link: https://lkml.kernel.org/r/20250923220652.568416-1-phillip@squashfs.org.uk
    Link: https://lkml.kernel.org/r/20250923220652.568416-2-phillip@squashfs.org.uk
    Signed-off-by: Phillip Lougher <phillip@squashfs.org.uk>
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Stable-dep-of: 9f1c14c1de1b ("Squashfs: reject negative file sizes in squashfs_read_inode()")
    Signed-off-by: Sasha Levin <sashal@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 7024b4a4809d0446281b56829fc9025854b0bd15
Author: Guenter Roeck <linux@roeck-us.net>
Date:   Mon Oct 6 13:18:57 2025 -0700

    ipmi: Fix handling of messages with provided receive message pointer
    
    commit e2c69490dda5d4c9f1bfbb2898989c8f3530e354 upstream.
    
    Prior to commit b52da4054ee0 ("ipmi: Rework user message limit handling"),
    i_ipmi_request() used to increase the user reference counter if the receive
    message is provided by the caller of IPMI API functions. This is no longer
    the case. However, ipmi_free_recv_msg() is still called and decreases the
    reference counter. This results in the reference counter reaching zero,
    the user data pointer is released, and all kinds of interesting crashes are
    seen.
    
    Fix the problem by increasing user reference counter if the receive message
    has been provided by the caller.
    
    Fixes: b52da4054ee0 ("ipmi: Rework user message limit handling")
    Reported-by: Eric Dumazet <edumazet@google.com>
    Cc: Eric Dumazet <edumazet@google.com>
    Cc: Greg Thelen <gthelen@google.com>
    Signed-off-by: Guenter Roeck <linux@roeck-us.net>
    Message-ID: <20251006201857.3433837-1-linux@roeck-us.net>
    Signed-off-by: Corey Minyard <corey@minyard.net>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit c6d254748b3083328dbbf874ed584c8b267a7928
Author: Jan Kara <jack@suse.cz>
Date:   Tue Oct 7 15:49:37 2025 +0200

    ext4: free orphan info with kvfree
    
    commit 971843c511c3c2f6eda96c6b03442913bfee6148 upstream.
    
    Orphan info is now getting allocated with kvmalloc_array(). Free it with
    kvfree() instead of kfree() to avoid complaints from mm.
    
    Reported-by: Chris Mason <clm@meta.com>
    Fixes: 0a6ce20c1564 ("ext4: verify orphan file size is not too big")
    Cc: stable@vger.kernel.org
    Signed-off-by: Jan Kara <jack@suse.cz>
    Message-ID: <20251007134936.7291-2-jack@suse.cz>
    Signed-off-by: Theodore Ts'o <tytso@mit.edu>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 45d88df89e118393033cbd9629f4cf6b26361ce4
Author: Huacai Chen <chenhuacai@kernel.org>
Date:   Fri Sep 12 21:54:53 2025 +0200

    ACPICA: Allow to skip Global Lock initialization
    
    commit feb8ae81b2378b75a99c81d315602ac8918ed382 upstream.
    
    Introduce acpi_gbl_use_global_lock, which allows to skip the Global Lock
    initialization. This is useful for systems without Global Lock (such as
    loong_arch), so as to avoid error messages during boot phase:
    
     ACPI Error: Could not enable global_lock event (20240827/evxfevnt-182)
     ACPI Error: No response from Global Lock hardware, disabling lock (20240827/evglock-59)
    
    Link: https://github.com/acpica/acpica/commit/463cb0fe
    Signed-off-by: Huacai Chen <chenhuacai@loongson.cn>
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Cc: Huacai Chen <chenhuacai@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a3e039869e98364068450980ab8bbff35dbc6c03
Author: Deepanshu Kartikey <kartikey406@gmail.com>
Date:   Tue Sep 23 19:02:45 2025 +0530

    ext4: validate ea_ino and size in check_xattrs
    
    commit 44d2a72f4d64655f906ba47a5e108733f59e6f28 upstream.
    
    During xattr block validation, check_xattrs() processes xattr entries
    without validating that entries claiming to use EA inodes have non-zero
    sizes. Corrupted filesystems may contain xattr entries where e_value_size
    is zero but e_value_inum is non-zero, indicating invalid xattr data.
    
    Add validation in check_xattrs() to detect this corruption pattern early
    and return -EFSCORRUPTED, preventing invalid xattr entries from causing
    issues throughout the ext4 codebase.
    
    Cc: stable@kernel.org
    Suggested-by: Theodore Ts'o <tytso@mit.edu>
    Reported-by: syzbot+4c9d23743a2409b80293@syzkaller.appspotmail.com
    Link: https://syzkaller.appspot.com/bug?extid=4c9d23743a2409b80293
    Signed-off-by: Deepanshu Kartikey <kartikey406@gmail.com>
    Signed-off-by: Theodore Ts'o <tytso@mit.edu>
    Message-ID: <20250923133245.1091761-1-kartikey406@gmail.com>
    Signed-off-by: Theodore Ts'o <tytso@mit.edu>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 440b003f449a4ff2a00b08c8eab9ba5cd28f3943
Author: Ahmet Eray Karadag <eraykrdg1@gmail.com>
Date:   Sat Sep 20 05:13:43 2025 +0300

    ext4: guard against EA inode refcount underflow in xattr update
    
    commit 57295e835408d8d425bef58da5253465db3d6888 upstream.
    
    syzkaller found a path where ext4_xattr_inode_update_ref() reads an EA
    inode refcount that is already <= 0 and then applies ref_change (often
    -1). That lets the refcount underflow and we proceed with a bogus value,
    triggering errors like:
    
      EXT4-fs error: EA inode <n> ref underflow: ref_count=-1 ref_change=-1
      EXT4-fs warning: ea_inode dec ref err=-117
    
    Make the invariant explicit: if the current refcount is non-positive,
    treat this as on-disk corruption, emit ext4_error_inode(), and fail the
    operation with -EFSCORRUPTED instead of updating the refcount. Delete the
    WARN_ONCE() as negative refcounts are now impossible; keep error reporting
    in ext4_error_inode().
    
    This prevents the underflow and the follow-on orphan/cleanup churn.
    
    Reported-by: syzbot+0be4f339a8218d2a5bb1@syzkaller.appspotmail.com
    Fixes: https://syzbot.org/bug?extid=0be4f339a8218d2a5bb1
    Cc: stable@kernel.org
    Co-developed-by: Albin Babu Varghese <albinbabuvarghese20@gmail.com>
    Signed-off-by: Albin Babu Varghese <albinbabuvarghese20@gmail.com>
    Signed-off-by: Ahmet Eray Karadag <eraykrdg1@gmail.com>
    Message-ID: <20250920021342.45575-1-eraykrdg1@gmail.com>
    Signed-off-by: Theodore Ts'o <tytso@mit.edu>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 3fb2b7550d0321edff92350592ee0e5eefb24808
Author: Zhang Yi <yi.zhang@huawei.com>
Date:   Fri Sep 12 18:58:41 2025 +0800

    ext4: fix an off-by-one issue during moving extents
    
    commit 12e803c8827d049ae8f2c743ef66ab87ae898375 upstream.
    
    During the movement of a written extent, mext_page_mkuptodate() is
    called to read data in the range [from, to) into the page cache and to
    update the corresponding buffers. Therefore, we should not wait on any
    buffer whose start offset is >= 'to'. Otherwise, it will return -EIO and
    fail the extents movement.
    
     $ for i in `seq 3 -1 0`; \
       do xfs_io -fs -c "pwrite -b 1024 $((i * 1024)) 1024" /mnt/foo; \
       done
     $ umount /mnt && mount /dev/pmem1s /mnt  # drop cache
     $ e4defrag /mnt/foo
       e4defrag 1.47.0 (5-Feb-2023)
       ext4 defragmentation for /mnt/foo
       [1/1]/mnt/foo:    0%    [ NG ]
       Success:                       [0/1]
    
    Cc: stable@kernel.org
    Fixes: a40759fb16ae ("ext4: remove array of buffer_heads from mext_page_mkuptodate()")
    Signed-off-by: Zhang Yi <yi.zhang@huawei.com>
    Reviewed-by: Jan Kara <jack@suse.cz>
    Message-ID: <20250912105841.1886799-1-yi.zhang@huaweicloud.com>
    Signed-off-by: Theodore Ts'o <tytso@mit.edu>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a6e94557cd05adc82fae0400f6e17745563e5412
Author: Theodore Ts'o <tytso@mit.edu>
Date:   Tue Sep 16 23:22:47 2025 -0400

    ext4: avoid potential buffer over-read in parse_apply_sb_mount_options()
    
    commit 8ecb790ea8c3fc69e77bace57f14cf0d7c177bd8 upstream.
    
    Unlike other strings in the ext4 superblock, we rely on tune2fs to
    make sure s_mount_opts is NUL terminated.  Harden
    parse_apply_sb_mount_options() by treating s_mount_opts as a potential
    __nonstring.
    
    Cc: stable@vger.kernel.org
    Fixes: 8b67f04ab9de ("ext4: Add mount options in superblock")
    Reviewed-by: Jan Kara <jack@suse.cz>
    Reviewed-by: Darrick J. Wong <djwong@kernel.org>
    Signed-off-by: Theodore Ts'o <tytso@mit.edu>
    Message-ID: <20250916-tune2fs-v2-1-d594dc7486f0@mit.edu>
    Signed-off-by: Theodore Ts'o <tytso@mit.edu>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 3ae197d84487ddd30ebab1819955933455d36d17
Author: Ojaswin Mujoo <ojaswin@linux.ibm.com>
Date:   Fri Sep 5 13:44:46 2025 +0530

    ext4: correctly handle queries for metadata mappings
    
    commit 46c22a8bb4cb03211da1100d7ee4a2005bf77c70 upstream.
    
    Currently, our handling of metadata is _ambiguous_ in some scenarios,
    that is, we end up returning unknown if the range only covers the
    mapping partially.
    
    For example, in the following case:
    
    $ xfs_io -c fsmap -d
    
      0: 254:16 [0..7]: static fs metadata 8
      1: 254:16 [8..15]: special 102:1 8
      2: 254:16 [16..5127]: special 102:2 5112
      3: 254:16 [5128..5255]: special 102:3 128
      4: 254:16 [5256..5383]: special 102:4 128
      5: 254:16 [5384..70919]: inodes 65536
      6: 254:16 [70920..70967]: unknown 48
      ...
    
    $ xfs_io -c fsmap -d 24 33
    
      0: 254:16 [24..39]: unknown 16  <--- incomplete reporting
    
    $ xfs_io -c fsmap -d 24 33  (With patch)
    
        0: 254:16 [16..5127]: special 102:2 5112
    
    This is because earlier in ext4_getfsmap_meta_helper, we end up ignoring
    any extent that starts before our queried range, but overlaps it. While
    the man page [1] is a bit ambiguous on this, this fix makes the output
    make more sense since we are anyways returning an "unknown" extent. This
    is also consistent to how XFS does it:
    
    $ xfs_io -c fsmap -d
    
      ...
      6: 254:16 [104..127]: free space 24
      7: 254:16 [128..191]: inodes 64
      ...
    
    $ xfs_io -c fsmap -d 137 150
    
      0: 254:16 [128..191]: inodes 64   <-- full extent returned
    
     [1] https://man7.org/linux/man-pages/man2/ioctl_getfsmap.2.html
    
    Reported-by: Ritesh Harjani (IBM) <ritesh.list@gmail.com>
    Cc: stable@kernel.org
    Signed-off-by: Ojaswin Mujoo <ojaswin@linux.ibm.com>
    Message-ID: <023f37e35ee280cd9baac0296cbadcbe10995cab.1757058211.git.ojaswin@linux.ibm.com>
    Signed-off-by: Theodore Ts'o <tytso@mit.edu>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit d33beb49b15f72245fc4aea6a5bfab1135584c7e
Author: Yongjian Sun <sunyongjian1@huawei.com>
Date:   Thu Sep 11 21:30:24 2025 +0800

    ext4: increase i_disksize to offset + len in ext4_update_disksize_before_punch()
    
    commit 9d80eaa1a1d37539224982b76c9ceeee736510b9 upstream.
    
    After running a stress test combined with fault injection,
    we performed fsck -a followed by fsck -fn on the filesystem
    image. During the second pass, fsck -fn reported:
    
    Inode 131512, end of extent exceeds allowed value
            (logical block 405, physical block 1180540, len 2)
    
    This inode was not in the orphan list. Analysis revealed the
    following call chain that leads to the inconsistency:
    
                                 ext4_da_write_end()
                                  //does not update i_disksize
                                 ext4_punch_hole()
                                  //truncate folio, keep size
    ext4_page_mkwrite()
     ext4_block_page_mkwrite()
      ext4_block_write_begin()
        ext4_get_block()
         //insert written extent without update i_disksize
    journal commit
    echo 1 > /sys/block/xxx/device/delete
    
    da-write path updates i_size but does not update i_disksize. Then
    ext4_punch_hole truncates the da-folio yet still leaves i_disksize
    unchanged(in the ext4_update_disksize_before_punch function, the
    condition offset + len < size is met). Then ext4_page_mkwrite sees
    ext4_nonda_switch return 1 and takes the nodioread_nolock path, the
    folio about to be written has just been punched out, and it’s offset
    sits beyond the current i_disksize. This may result in a written
    extent being inserted, but again does not update i_disksize. If the
    journal gets committed and then the block device is yanked, we might
    run into this. It should be noted that replacing ext4_punch_hole with
    ext4_zero_range in the call sequence may also trigger this issue, as
    neither will update i_disksize under these circumstances.
    
    To fix this, we can modify ext4_update_disksize_before_punch to
    increase i_disksize to min(i_size, offset + len) when both i_size and
    (offset + len) are greater than i_disksize.
    
    Cc: stable@kernel.org
    Signed-off-by: Yongjian Sun <sunyongjian1@huawei.com>
    Reviewed-by: Zhang Yi <yi.zhang@huawei.com>
    Reviewed-by: Jan Kara <jack@suse.cz>
    Reviewed-by: Baokun Li <libaokun1@huawei.com>
    Message-ID: <20250911133024.1841027-1-sunyongjian@huaweicloud.com>
    Signed-off-by: Theodore Ts'o <tytso@mit.edu>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 2b9da798ff0f4d026c5f0f815047393ebe7d8859
Author: Jan Kara <jack@suse.cz>
Date:   Tue Sep 9 13:22:07 2025 +0200

    ext4: verify orphan file size is not too big
    
    commit 0a6ce20c156442a4ce2a404747bb0fb05d54eeb3 upstream.
    
    In principle orphan file can be arbitrarily large. However orphan replay
    needs to traverse it all and we also pin all its buffers in memory. Thus
    filesystems with absurdly large orphan files can lead to big amounts of
    memory consumed. Limit orphan file size to a sane value and also use
    kvmalloc() for allocating array of block descriptor structures to avoid
    large order allocations for sane but large orphan files.
    
    Reported-by: syzbot+0b92850d68d9b12934f5@syzkaller.appspotmail.com
    Fixes: 02f310fcf47f ("ext4: Speedup ext4 orphan inode handling")
    Cc: stable@kernel.org
    Signed-off-by: Jan Kara <jack@suse.cz>
    Message-ID: <20250909112206.10459-2-jack@suse.cz>
    Signed-off-by: Theodore Ts'o <tytso@mit.edu>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit e9663669a5fa1ee5aeb1036fdcfb8ab6aa4bbfbc
Author: Jan Kara <jack@suse.cz>
Date:   Mon Sep 1 13:27:40 2025 +0200

    ext4: fail unaligned direct IO write with EINVAL
    
    commit 963845748fe67125006859229487b45485564db7 upstream.
    
    Commit bc264fea0f6f ("iomap: support incremental iomap_iter advances")
    changed the error handling logic in iomap_iter(). Previously any error
    from iomap_dio_bio_iter() got propagated to userspace, after this commit
    if ->iomap_end returns error, it gets propagated to userspace instead of
    an error from iomap_dio_bio_iter(). This results in unaligned writes to
    ext4 to silently fallback to buffered IO instead of erroring out.
    
    Now returning ENOTBLK for DIO writes from ext4_iomap_end() seems
    unnecessary these days. It is enough to return ENOTBLK from
    ext4_iomap_begin() when we don't support DIO write for that particular
    file offset (due to hole).
    
    Fixes: bc264fea0f6f ("iomap: support incremental iomap_iter advances")
    Cc: stable@kernel.org
    Signed-off-by: Jan Kara <jack@suse.cz>
    Reviewed-by: Ritesh Harjani (IBM) <ritesh.list@gmail.com>
    Message-ID: <20250901112739.32484-2-jack@suse.cz>
    Signed-off-by: Theodore Ts'o <tytso@mit.edu>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit d9774bbe39bf65f5854752d27130112b6adbf355
Author: Baokun Li <libaokun1@huawei.com>
Date:   Thu Aug 21 21:38:57 2025 +0800

    ext4: add ext4_sb_bread_nofail() helper function for ext4_free_branches()
    
    commit d8b90e6387a74bcb1714c8d1e6a782ff709de9a9 upstream.
    
    The implicit __GFP_NOFAIL flag in ext4_sb_bread() was removed in commit
    8a83ac54940d ("ext4: call bdev_getblk() from sb_getblk_gfp()"), meaning
    the function can now fail under memory pressure.
    
    Most callers of ext4_sb_bread() propagate the error to userspace and do not
    remount the filesystem read-only. However, ext4_free_branches() handles
    ext4_sb_bread() failure by remounting the filesystem read-only.
    
    This implies that an ext3 filesystem (mounted via the ext4 driver) could be
    forcibly remounted read-only due to a transient page allocation failure,
    which is unacceptable.
    
    To mitigate this, introduce a new helper function, ext4_sb_bread_nofail(),
    which explicitly uses __GFP_NOFAIL, and use it in ext4_free_branches().
    
    Fixes: 8a83ac54940d ("ext4: call bdev_getblk() from sb_getblk_gfp()")
    Cc: stable@kernel.org
    Signed-off-by: Baokun Li <libaokun1@huawei.com>
    Reviewed-by: Jan Kara <jack@suse.cz>
    Signed-off-by: Theodore Ts'o <tytso@mit.edu>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 8699bc1b67ec5e0ebd865aa5b9f1be14a68f1d2d
Author: Dikshita Agarwal <dikshita.agarwal@oss.qualcomm.com>
Date:   Mon Aug 25 12:30:33 2025 +0530

    media: iris: Allow stop on firmware only if start was issued.
    
    commit 56a2d85ee8f9b994e5cd17039133218c57c5902b upstream.
    
    For HFI Gen1, the instances substate is changed to LOAD_RESOURCES only
    when a START command is issues to the firmware. If STOP is called
    without a prior START, the firmware may reject the command and throw
    some erros.
    Handle this by adding a substate check before issuing STOP command to
    the firmware.
    
    Fixes: 11712ce70f8e ("media: iris: implement vb2 streaming ops")
    Cc: stable@vger.kernel.org
    Reviewed-by: Vikash Garodia <quic_vgarodia@quicinc.com>
    Tested-by: Vikash Garodia <quic_vgarodia@quicinc.com> # X1E80100
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8550-HDK
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8650-HDK
    Signed-off-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Tested-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org> # x1e80100-crd
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit bb3b3ad142aa98211248bf52954730f0340343df
Author: Dikshita Agarwal <dikshita.agarwal@oss.qualcomm.com>
Date:   Mon Aug 25 12:30:36 2025 +0530

    media: iris: Fix format check for CAPTURE plane in try_fmt
    
    commit 2dbd2645c07df8de04ee37b24f2395800513391e upstream.
    
    Previously, the format validation relied on an array of supported
    formats, which only listed formats for the OUTPUT plane. This caused
    failures when validating formats for the CAPTURE plane.
    Update the check to validate against the only supported format on the
    CAPTURE plane, which is NV12.
    
    Fixes: fde6161d91bb ("media: iris: Add HEVC and VP9 formats for decoder")
    Cc: stable@vger.kernel.org
    Reviewed-by: Vikash Garodia <quic_vgarodia@quicinc.com>
    Tested-by: Vikash Garodia <quic_vgarodia@quicinc.com> # X1E80100
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8550-HDK
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8650-HDK
    Signed-off-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Tested-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org> # x1e80100-crd
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 33114cf0d652f7f7bc61c1a56cf53ce3cbdcb1e3
Author: Dikshita Agarwal <dikshita.agarwal@oss.qualcomm.com>
Date:   Mon Aug 25 12:30:35 2025 +0530

    media: iris: Fix missing LAST flag handling during drain
    
    commit 8172f57746d68e5c3c743f725435d75c5a4db1ac upstream.
    
    Improve drain handling by ensuring the LAST flag is attached to final
    capture buffer when drain response is received from the firmware.
    
    Previously, the driver failed to attach the V4L2_BUF_FLAG_LAST flag when
    a drain response was received from the firmware, relying on userspace to
    mark the next queued buffer as LAST. This update fixes the issue by
    checking the pending drain status, attaching the LAST flag to the
    capture buffer received from the firmware (with EOS attached), and
    returning it to the V4L2 layer correctly.
    
    Fixes: d09100763bed ("media: iris: add support for drain sequence")
    Cc: stable@vger.kernel.org
    Reviewed-by: Vikash Garodia <quic_vgarodia@quicinc.com>
    Tested-by: Vikash Garodia <quic_vgarodia@quicinc.com> # X1E80100
    Reviewed-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org>
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8550-HDK
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8650-HDK
    Signed-off-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Tested-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org> # x1e80100-crd
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 44fb0daf3afcfff939d31610e94078e7ee7b95c0
Author: Dikshita Agarwal <dikshita.agarwal@oss.qualcomm.com>
Date:   Mon Aug 25 12:30:34 2025 +0530

    media: iris: Send dummy buffer address for all codecs during drain
    
    commit dec073dd8452e174a69db8444e0932e6b4f31c99 upstream.
    
    Firmware can handle a dummy address for buffers with the EOS flag. To
    ensure consistent behavior across all codecs, update the drain
    command to always send a dummy buffer address.
    
    This makes the drain handling uniform and avoids any codec specific
    assumptions.
    
    Fixes: 478c4478610d ("media: iris: Add codec specific check for VP9 decoder drain handling")
    Cc: stable@vger.kernel.org
    Reviewed-by: Vikash Garodia <quic_vgarodia@quicinc.com>
    Tested-by: Vikash Garodia <quic_vgarodia@quicinc.com> # X1E80100
    Reviewed-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org>
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8550-HDK
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8650-HDK
    Signed-off-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Tested-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org> # x1e80100-crd
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit c9a4747fe069edfb03a20b0d65952263310e90d5
Author: Dikshita Agarwal <dikshita.agarwal@oss.qualcomm.com>
Date:   Mon Aug 25 12:30:31 2025 +0530

    media: iris: Update vbuf flags before v4l2_m2m_buf_done
    
    commit 8a432174ac263fb9dd93d232b99c84e430e6d6b5 upstream.
    
    Update the vbuf flags appropriately in error cases before calling
    v4l2_m2m_buf_done(). Previously, the flag update was skippied in error
    scenario, which could result in incorrect state reporting for buffers.
    
    Fixes: 17f2a485ca67 ("media: iris: implement vb2 ops for buf_queue and firmware response")
    Cc: stable@vger.kernel.org
    Reviewed-by: Vikash Garodia <quic_vgarodia@quicinc.com>
    Tested-by: Vikash Garodia <quic_vgarodia@quicinc.com> # X1E80100
    Reviewed-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org>
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8550-HDK
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8650-HDK
    Signed-off-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Tested-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org> # x1e80100-crd
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f4e513181dda97ce5fa222fce4bfdd930c8c1efb
Author: Dikshita Agarwal <dikshita.agarwal@oss.qualcomm.com>
Date:   Mon Aug 25 12:30:32 2025 +0530

    media: iris: Simplify session stop logic by relying on vb2 checks
    
    commit 0fe10666d3b4d0757b7f4671892523855ee68cc8 upstream.
    
    Remove earlier complex conditional checks in the non-streaming path that
    attempted to verify if stop was called on a plane that was previously
    started. These explicit checks are redundant, as vb2 already ensures
    that stop is only called on ports that have been started, maintaining
    correct buffer state management.
    
    Fixes: 11712ce70f8e ("media: iris: implement vb2 streaming ops")
    Cc: stable@vger.kernel.org
    Reviewed-by: Vikash Garodia <quic_vgarodia@quicinc.com>
    Tested-by: Vikash Garodia <quic_vgarodia@quicinc.com> # X1E80100
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8550-HDK
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8650-HDK
    Signed-off-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Tested-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org> # x1e80100-crd
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 1c39ea9b487318612046fb1b08cb54ca350a4c5e
Author: Dikshita Agarwal <dikshita.agarwal@oss.qualcomm.com>
Date:   Mon Aug 25 12:30:30 2025 +0530

    media: iris: Always destroy internal buffers on firmware release response
    
    commit 9cae3619e465dd1cdaa5a5ffbbaf4f41338b0022 upstream.
    
    Currently, internal buffers are destroyed only if 'PENDING_RELEASE' flag
    is set when a release response is received from the firmware, which is
    incorrect. Internal buffers should always be destroyed when the firmware
    explicitly releases it, regardless of whether the 'PENDING_RELEASE' flag
    was set by the driver. This is specially important during force-stop
    scenarios, where the firmware may release buffers without driver marking
    them for release.
    Fix this by removing the incorrect check and ensuring all buffers are
    properly cleaned up.
    
    Fixes: 73702f45db81 ("media: iris: allocate, initialize and queue internal buffers")
    Cc: stable@vger.kernel.org
    Reviewed-by: Vikash Garodia <quic_vgarodia@quicinc.com>
    Tested-by: Vikash Garodia <quic_vgarodia@quicinc.com> # X1E80100
    Reviewed-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org>
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8550-HDK
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8650-HDK
    Signed-off-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Tested-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org> # x1e80100-crd
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit cf0a3a48fcc4b74502475b64461f240dc31da081
Author: Dikshita Agarwal <dikshita.agarwal@oss.qualcomm.com>
Date:   Mon Aug 25 12:30:29 2025 +0530

    media: iris: Allow substate transition to load resources during output streaming
    
    commit 65f72c6a8d97c0cbdc785cb9a35dc358dee67959 upstream.
    
    A client (e.g., GST for encoder) can initiate streaming on the capture
    port before the output port, causing the instance state to transition to
    OUTPUT_STREAMING. When streaming is subsequently started on the output
    port, the instance state advances to STREAMING, and the substate should
    transition to LOAD_RESOURCES.
    
    Previously, the code blocked the substate transition to LOAD_RESOURCES
    if the instance state was OUTPUT_STREAMING. This update modifies the
    logic to permit the substate transition to LOAD_RESOURCES when the
    instance state is OUTPUT_STREAMING, thereby supporting this client
    streaming sequence.
    
    Fixes: 547f7b8c5090 ("media: iris: add check to allow sub states transitions")
    Cc: stable@vger.kernel.org
    Reviewed-by: Vikash Garodia <quic_vgarodia@quicinc.com>
    Tested-by: Vikash Garodia <quic_vgarodia@quicinc.com> # X1E80100
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8550-HDK
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8650-HDK
    Signed-off-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Tested-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org> # x1e80100-crd
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f92682a11c66cd3f5bce10964182c2751d39677b
Author: Dikshita Agarwal <dikshita.agarwal@oss.qualcomm.com>
Date:   Mon Aug 25 12:30:25 2025 +0530

    media: iris: Fix buffer count reporting in internal buffer check
    
    commit cba6aed4223e83ae0f2ed1c0f68d974fd62847bc upstream.
    
    Initialize the count variable to zero before counting unreleased
    internal buffers in iris_check_num_queued_internal_buffers().
    This prevents stale values from previous iterations and ensures accurate
    error reporting for each buffer type. Without this initialization, the
    count could accumulate across types, leading to incorrect log messages.
    
    Fixes: d2abb1ff5a3c ("media: iris: Verify internal buffer release on close")
    Cc: stable@vger.kernel.org
    Reviewed-by: Vikash Garodia <quic_vgarodia@quicinc.com>
    Tested-by: Vikash Garodia <quic_vgarodia@quicinc.com> # X1E80100
    Reviewed-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org>
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8550-HDK
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8650-HDK
    Signed-off-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Tested-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org> # x1e80100-crd
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit ff618ceda060a9b0a61b076dcc635ea6a45e3f42
Author: Dikshita Agarwal <dikshita.agarwal@oss.qualcomm.com>
Date:   Mon Aug 25 12:30:28 2025 +0530

    media: iris: Fix port streaming handling
    
    commit 4b67ef9b333ed645879b4b1a11e35e019ff4cfea upstream.
    
    The previous check to block capture port streaming before output port
    was incorrect and caused some valid usecase to fail. While removing that
    check allows capture port to enter streaming independently, it also
    introduced firmware errors due to premature queuing of DPB buffers
    before the firmware session was fully started which happens only when
    streamon is called on output port.
    
    Fix this by deferring DPB buffer queuing to the firmware until both
    capture and output are streaming and state is 'STREAMING'.
    
    Fixes: 11712ce70f8e ("media: iris: implement vb2 streaming ops")
    Cc: stable@vger.kernel.org
    Reviewed-by: Vikash Garodia <quic_vgarodia@quicinc.com>
    Tested-by: Vikash Garodia <quic_vgarodia@quicinc.com> # X1E80100
    Reviewed-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org>
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8550-HDK
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8650-HDK
    Signed-off-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Tested-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org> # x1e80100-crd
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 78728f1f3f52fe3ade60dad199784ab35dc787dd
Author: Dikshita Agarwal <dikshita.agarwal@oss.qualcomm.com>
Date:   Fri Aug 22 11:23:30 2025 +0530

    media: iris: vpu3x: Add MNoC low power handshake during hardware power-off
    
    commit 93fad55aa996eef17a837ed95b1d621ef05d967b upstream.
    
    Add the missing write to AON_WRAPPER_MVP_NOC_LPI_CONTROL before
    reading the LPI status register. Introduce a handshake loop to ensure
    MNoC enters low power mode reliably during VPU3 hardware power-off with
    timeout handling.
    
    Fixes: 02083a1e00ae ("media: platform: qcom/iris: add support for vpu33")
    Cc: stable@vger.kernel.org
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8650-QRD
    Tested-by: Neil Armstrong <neil.armstrong@linaro.org> # on SM8650-HDK
    Reviewed-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org>
    Signed-off-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 7a0a77b936ff28f59c271172e81cefebf7b2b7a6
Author: Neil Armstrong <neil.armstrong@linaro.org>
Date:   Fri Aug 22 11:20:01 2025 +0200

    media: iris: fix module removal if firmware download failed
    
    commit fde38008fc4f43db8c17869491870df24b501543 upstream.
    
    Fix remove if firmware failed to load:
    qcom-iris aa00000.video-codec: Direct firmware load for qcom/vpu/vpu33_p4.mbn failed with error -2
    qcom-iris aa00000.video-codec: firmware download failed
    qcom-iris aa00000.video-codec: core init failed
    
    then:
    $ echo aa00000.video-codec > /sys/bus/platform/drivers/qcom-iris/unbind
    
    Triggers:
    genpd genpd:1:aa00000.video-codec: Runtime PM usage count underflow!
    ------------[ cut here ]------------
    video_cc_mvs0_clk already disabled
    WARNING: drivers/clk/clk.c:1206 at clk_core_disable+0xa4/0xac, CPU#1: sh/542
    <snip>
    pc : clk_core_disable+0xa4/0xac
    lr : clk_core_disable+0xa4/0xac
    <snip>
    Call trace:
     clk_core_disable+0xa4/0xac (P)
     clk_disable+0x30/0x4c
     iris_disable_unprepare_clock+0x20/0x48 [qcom_iris]
     iris_vpu_power_off_hw+0x48/0x58 [qcom_iris]
     iris_vpu33_power_off_hardware+0x44/0x230 [qcom_iris]
     iris_vpu_power_off+0x34/0x84 [qcom_iris]
     iris_core_deinit+0x44/0xc8 [qcom_iris]
     iris_remove+0x20/0x48 [qcom_iris]
     platform_remove+0x20/0x30
     device_remove+0x4c/0x80
    <snip>
    ---[ end trace 0000000000000000 ]---
    ------------[ cut here ]------------
    video_cc_mvs0_clk already unprepared
    WARNING: drivers/clk/clk.c:1065 at clk_core_unprepare+0xf0/0x110, CPU#2: sh/542
    <snip>
    pc : clk_core_unprepare+0xf0/0x110
    lr : clk_core_unprepare+0xf0/0x110
    <snip>
    Call trace:
     clk_core_unprepare+0xf0/0x110 (P)
     clk_unprepare+0x2c/0x44
     iris_disable_unprepare_clock+0x28/0x48 [qcom_iris]
     iris_vpu_power_off_hw+0x48/0x58 [qcom_iris]
     iris_vpu33_power_off_hardware+0x44/0x230 [qcom_iris]
     iris_vpu_power_off+0x34/0x84 [qcom_iris]
     iris_core_deinit+0x44/0xc8 [qcom_iris]
     iris_remove+0x20/0x48 [qcom_iris]
     platform_remove+0x20/0x30
     device_remove+0x4c/0x80
    <snip>
    ---[ end trace 0000000000000000 ]---
    genpd genpd:0:aa00000.video-codec: Runtime PM usage count underflow!
    ------------[ cut here ]------------
    gcc_video_axi0_clk already disabled
    WARNING: drivers/clk/clk.c:1206 at clk_core_disable+0xa4/0xac, CPU#4: sh/542
    <snip>
    pc : clk_core_disable+0xa4/0xac
    lr : clk_core_disable+0xa4/0xac
    <snip>
    Call trace:
     clk_core_disable+0xa4/0xac (P)
     clk_disable+0x30/0x4c
     iris_disable_unprepare_clock+0x20/0x48 [qcom_iris]
     iris_vpu33_power_off_controller+0x17c/0x428 [qcom_iris]
     iris_vpu_power_off+0x48/0x84 [qcom_iris]
     iris_core_deinit+0x44/0xc8 [qcom_iris]
     iris_remove+0x20/0x48 [qcom_iris]
     platform_remove+0x20/0x30
     device_remove+0x4c/0x80
    <snip>
    ------------[ cut here ]------------
    gcc_video_axi0_clk already unprepared
    WARNING: drivers/clk/clk.c:1065 at clk_core_unprepare+0xf0/0x110, CPU#4: sh/542
    <snip>
    pc : clk_core_unprepare+0xf0/0x110
    lr : clk_core_unprepare+0xf0/0x110
    <snip>
    Call trace:
     clk_core_unprepare+0xf0/0x110 (P)
     clk_unprepare+0x2c/0x44
     iris_disable_unprepare_clock+0x28/0x48 [qcom_iris]
     iris_vpu33_power_off_controller+0x17c/0x428 [qcom_iris]
     iris_vpu_power_off+0x48/0x84 [qcom_iris]
     iris_core_deinit+0x44/0xc8 [qcom_iris]
     iris_remove+0x20/0x48 [qcom_iris]
     platform_remove+0x20/0x30
     device_remove+0x4c/0x80
    <snip>
    ---[ end trace 0000000000000000 ]---
    
    Skip deinit if initialization never succeeded.
    
    Fixes: d7378f84e94e ("media: iris: introduce iris core state management with shared queues")
    Fixes: d19b163356b8 ("media: iris: implement video firmware load/unload")
    Fixes: bb8a95aa038e ("media: iris: implement power management")
    Cc: stable@vger.kernel.org
    Reviewed-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Reviewed-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org>
    Signed-off-by: Neil Armstrong <neil.armstrong@linaro.org>
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit e1aba6510016ae5018c945066f4a0d7b2bba8398
Author: Stephan Gerhold <stephan.gerhold@linaro.org>
Date:   Mon Aug 18 11:50:41 2025 +0200

    media: iris: Fix firmware reference leak and unmap memory after load
    
    commit 57429b0fddfe3cea21a56326576451a4a4c2019b upstream.
    
    When we succeed loading the firmware, we don't want to hold on to the
    firmware pointer anymore, since it won't be freed anywhere else. The same
    applies for the mapped memory. Unmapping the memory is particularly
    important since the memory will be protected after the Iris firmware is
    started, so we need to make sure there will be no accidental access to this
    region (even if just a speculative one from the CPU).
    
    Almost the same firmware loading code also exists in venus/firmware.c,
    there it is implemented correctly.
    
    Fix this by dropping the early "return ret" and move the call of
    qcom_scm_pas_auth_and_reset() out of iris_load_fw_to_memory(). We should
    unmap the memory before bringing the firmware out of reset.
    
    Cc: stable@vger.kernel.org
    Fixes: d19b163356b8 ("media: iris: implement video firmware load/unload")
    Signed-off-by: Stephan Gerhold <stephan.gerhold@linaro.org>
    Reviewed-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org>
    Reviewed-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 3c872ba73c2a2e97e9c448383e67a03ae745a685
Author: Krzysztof Kozlowski <krzysztof.kozlowski@linaro.org>
Date:   Wed Jul 2 15:41:58 2025 +0200

    media: iris: Call correct power off callback in cleanup path
    
    commit 2fbb823a0744665fe6015bd03d435bd334ccecf7 upstream.
    
    Driver implements different callbacks for the power off controller
    (.power_off_controller):
    
     - iris_vpu_power_off_controller,
     - iris_vpu33_power_off_controller,
    
    The generic wrapper for handling power off - iris_vpu_power_off() -
    calls them via 'iris_platform_data->vpu_ops', so shall the cleanup code
    in iris_vpu_power_on().
    
    This makes also sense if looking at caller of iris_vpu_power_on(), which
    unwinds also with the wrapper calling respective platfortm code (unwinds
    with iris_vpu_power_off()).
    
    Otherwise power off sequence on the newer VPU3.3 in error path is not
    complete.
    
    Fixes: c69df5de4ac3 ("media: platform: qcom/iris: add power_off_controller to vpu_ops")
    Cc: stable@vger.kernel.org
    Signed-off-by: Krzysztof Kozlowski <krzysztof.kozlowski@linaro.org>
    Reviewed-by: Vikash Garodia <quic_vgarodia@quicinc.com>
    Reviewed-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org>
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 6c3c870e8d705c428a3a1b9c484342915e7a8140
Author: Olga Kornievskaia <okorniev@redhat.com>
Date:   Thu Aug 21 16:31:46 2025 -0400

    nfsd: nfserr_jukebox in nlm_fopen should lead to a retry
    
    commit a082e4b4d08a4a0e656d90c2c05da85f23e6d0c9 upstream.
    
    When v3 NLM request finds a conflicting delegation, it triggers
    a delegation recall and nfsd_open fails with EAGAIN. nfsd_open
    then translates EAGAIN into nfserr_jukebox. In nlm_fopen, instead
    of returning nlm_failed for when there is a conflicting delegation,
    drop this NLM request so that the client retries. Once delegation
    is recalled and if a local lock is claimed, a retry would lead to
    nfsd returning a nlm_lck_blocked error or a successful nlm lock.
    
    Fixes: d343fce148a4 ("[PATCH] knfsd: Allow lockd to drop replies as appropriate")
    Cc: stable@vger.kernel.org # v6.6
    Signed-off-by: Olga Kornievskaia <okorniev@redhat.com>
    Signed-off-by: Chuck Lever <chuck.lever@oracle.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 9e05bc6daf95d6a64ca99c93d8db1b90f5691654
Author: Thorsten Blum <thorsten.blum@linux.dev>
Date:   Wed Aug 6 03:10:01 2025 +0200

    NFSD: Fix destination buffer size in nfsd4_ssc_setup_dul()
    
    commit ab1c282c010c4f327bd7addc3c0035fd8e3c1721 upstream.
    
    Commit 5304877936c0 ("NFSD: Fix strncpy() fortify warning") replaced
    strncpy(,, sizeof(..)) with strlcpy(,, sizeof(..) - 1), but strlcpy()
    already guaranteed NUL-termination of the destination buffer and
    subtracting one byte potentially truncated the source string.
    
    The incorrect size was then carried over in commit 72f78ae00a8e ("NFSD:
    move from strlcpy with unused retval to strscpy") when switching from
    strlcpy() to strscpy().
    
    Fix this off-by-one error by using the full size of the destination
    buffer again.
    
    Cc: stable@vger.kernel.org
    Fixes: 5304877936c0 ("NFSD: Fix strncpy() fortify warning")
    Signed-off-by: Thorsten Blum <thorsten.blum@linux.dev>
    Signed-off-by: Chuck Lever <chuck.lever@oracle.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 526213bd432649a22c8213a1fa0ff2825b8299d0
Author: Scott Mayhew <smayhew@redhat.com>
Date:   Wed Aug 6 15:15:43 2025 -0400

    nfsd: decouple the xprtsec policy check from check_nfsd_access()
    
    commit e4f574ca9c6dfa66695bb054ff5df43ecea873ec upstream.
    
    A while back I had reported that an NFSv3 client could successfully
    mount using '-o xprtsec=none' an export that had been exported with
    'xprtsec=tls:mtls'.  By "successfully" I mean that the mount command
    would succeed and the mount would show up in /proc/mount.  Attempting
    to do anything futher with the mount would be met with NFS3ERR_ACCES.
    
    This was fixed (albeit accidentally) by commit bb4f07f2409c ("nfsd:
    Fix NFSD_MAY_BYPASS_GSS and NFSD_MAY_BYPASS_GSS_ON_ROOT") and was
    subsequently re-broken by commit 0813c5f01249 ("nfsd: fix access
    checking for NLM under XPRTSEC policies").
    
    Transport Layer Security isn't an RPC security flavor or pseudo-flavor,
    so we shouldn't be conflating them when determining whether the access
    checks can be bypassed.  Split check_nfsd_access() into two helpers, and
    have __fh_verify() call the helpers directly since __fh_verify() has
    logic that allows one or both of the checks to be skipped.  All other
    sites will continue to call check_nfsd_access().
    
    Link: https://lore.kernel.org/linux-nfs/ZjO3Qwf_G87yNXb2@aion/
    Fixes: 9280c5774314 ("NFSD: Handle new xprtsec= export option")
    Cc: stable@vger.kernel.org
    Signed-off-by: Scott Mayhew <smayhew@redhat.com>
    Signed-off-by: Chuck Lever <chuck.lever@oracle.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 5adaa3bea8b9bc3749c742fb64e930bfaba19fba
Author: SeongJae Park <sj@kernel.org>
Date:   Mon Sep 15 20:15:49 2025 -0700

    mm/damon/lru_sort: use param_ctx for damon_attrs staging
    
    commit e18190b7e97e9db6546390e6e0ceddae606892b2 upstream.
    
    damon_lru_sort_apply_parameters() allocates a new DAMON context, stages
    user-specified DAMON parameters on it, and commits to running DAMON
    context at once, using damon_commit_ctx().  The code is, however, directly
    updating the monitoring attributes of the running context.  And the
    attributes are over-written by later damon_commit_ctx() call.  This means
    that the monitoring attributes parameters are not really working.  Fix the
    wrong use of the parameter context.
    
    Link: https://lkml.kernel.org/r/20250916031549.115326-1-sj@kernel.org
    Fixes: a30969436428 ("mm/damon/lru_sort: use damon_commit_ctx()")
    Signed-off-by: SeongJae Park <sj@kernel.org>
    Reviewed-by: Joshua Hahn <joshua.hahnjy@gmail.com>
    Cc: Joshua Hahn <joshua.hahnjy@gmail.com>
    Cc: <stable@vger.kernel.org>    [6.11+]
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 0ccd91cf749536d41307a07e60ec14ab0dbf21f5
Author: SeongJae Park <sj@kernel.org>
Date:   Mon Sep 29 17:44:09 2025 -0700

    mm/damon/vaddr: do not repeat pte_offset_map_lock() until success
    
    commit b93af2cc8e036754c0d9970d9ddc47f43cc94b9f upstream.
    
    DAMON's virtual address space operation set implementation (vaddr) calls
    pte_offset_map_lock() inside the page table walk callback function.  This
    is for reading and writing page table accessed bits.  If
    pte_offset_map_lock() fails, it retries by returning the page table walk
    callback function with ACTION_AGAIN.
    
    pte_offset_map_lock() can continuously fail if the target is a pmd
    migration entry, though.  Hence it could cause an infinite page table walk
    if the migration cannot be done until the page table walk is finished.
    This indeed caused a soft lockup when CPU hotplugging and DAMON were
    running in parallel.
    
    Avoid the infinite loop by simply not retrying the page table walk.  DAMON
    is promising only a best-effort accuracy, so missing access to such pages
    is no problem.
    
    Link: https://lkml.kernel.org/r/20250930004410.55228-1-sj@kernel.org
    Fixes: 7780d04046a2 ("mm/pagewalkers: ACTION_AGAIN if pte_offset_map_lock() fails")
    Signed-off-by: SeongJae Park <sj@kernel.org>
    Reported-by: Xinyu Zheng <zhengxinyu6@huawei.com>
    Closes: https://lore.kernel.org/20250918030029.2652607-1-zhengxinyu6@huawei.com
    Acked-by: Hugh Dickins <hughd@google.com>
    Cc: <stable@vger.kernel.org>    [6.5+]
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit ed30038550014a2d8ea6d7cc3de483aaa269d2e3
Author: Li RongQing <lirongqing@baidu.com>
Date:   Thu Aug 14 18:23:33 2025 +0800

    mm/hugetlb: early exit from hugetlb_pages_alloc_boot() when max_huge_pages=0
    
    commit b322e88b3d553e85b4e15779491c70022783faa4 upstream.
    
    Optimize hugetlb_pages_alloc_boot() to return immediately when
    max_huge_pages is 0, avoiding unnecessary CPU cycles and the below log
    message when hugepages aren't configured in the kernel command line.
    [    3.702280] HugeTLB: allocation took 0ms with hugepage_allocation_threads=32
    
    Link: https://lkml.kernel.org/r/20250814102333.4428-1-lirongqing@baidu.com
    Signed-off-by: Li RongQing <lirongqing@baidu.com>
    Reviewed-by: Dev Jain <dev.jain@arm.com>
    Tested-by: Dev Jain <dev.jain@arm.com>
    Reviewed-by: Jane Chu <jane.chu@oracle.com>
    Acked-by: David Hildenbrand <david@redhat.com>
    Cc: Muchun Song <muchun.song@linux.dev>
    Cc: Oscar Salvador <osalvador@suse.de>
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit b5d0b85afb032621fc6d960ceb9a2242f8fe9396
Author: Thadeu Lima de Souza Cascardo <cascardo@igalia.com>
Date:   Thu Aug 14 14:22:45 2025 -0300

    mm/page_alloc: only set ALLOC_HIGHATOMIC for __GPF_HIGH allocations
    
    commit 6a204d4b14c99232e05d35305c27ebce1c009840 upstream.
    
    Commit 524c48072e56 ("mm/page_alloc: rename ALLOC_HIGH to
    ALLOC_MIN_RESERVE") is the start of a series that explains how __GFP_HIGH,
    which implies ALLOC_MIN_RESERVE, is going to be used instead of
    __GFP_ATOMIC for high atomic reserves.
    
    Commit eb2e2b425c69 ("mm/page_alloc: explicitly record high-order atomic
    allocations in alloc_flags") introduced ALLOC_HIGHATOMIC for such
    allocations of order higher than 0.  It still used __GFP_ATOMIC, though.
    
    Then, commit 1ebbb21811b7 ("mm/page_alloc: explicitly define how
    __GFP_HIGH non-blocking allocations accesses reserves") just turned that
    check for !__GFP_DIRECT_RECLAIM, ignoring that high atomic reserves were
    expected to test for __GFP_HIGH.
    
    This leads to high atomic reserves being added for high-order GFP_NOWAIT
    allocations and others that clear __GFP_DIRECT_RECLAIM, which is
    unexpected.  Later, those reserves lead to 0-order allocations going to
    the slow path and starting reclaim.
    
    From /proc/pagetypeinfo, without the patch:
    
    Node    0, zone      DMA, type   HighAtomic      0      0      0      0      0      0      0      0      0      0      0
    Node    0, zone    DMA32, type   HighAtomic      1      8     10      9      7      3      0      0      0      0      0
    Node    0, zone   Normal, type   HighAtomic     64     20     12      5      0      0      0      0      0      0      0
    
    With the patch:
    
    Node    0, zone      DMA, type   HighAtomic      0      0      0      0      0      0      0      0      0      0      0
    Node    0, zone    DMA32, type   HighAtomic      0      0      0      0      0      0      0      0      0      0      0
    Node    0, zone   Normal, type   HighAtomic      0      0      0      0      0      0      0      0      0      0      0
    
    Link: https://lkml.kernel.org/r/20250814172245.1259625-1-cascardo@igalia.com
    Fixes: 1ebbb21811b7 ("mm/page_alloc: explicitly define how __GFP_HIGH non-blocking allocations accesses reserves")
    Signed-off-by: Thadeu Lima de Souza Cascardo <cascardo@igalia.com>
    Tested-by: Helen Koike <koike@igalia.com>
    Reviewed-by: Vlastimil Babka <vbabka@suse.cz>
    Tested-by: Sergey Senozhatsky <senozhatsky@chromium.org>
    Acked-by: Michal Hocko <mhocko@suse.com>
    Cc: Mel Gorman <mgorman@techsingularity.net>
    Cc: Matthew Wilcox <willy@infradead.org>
    Cc: NeilBrown <neilb@suse.de>
    Cc: Thierry Reding <thierry.reding@gmail.com>
    Cc: Brendan Jackman <jackmanb@google.com>
    Cc: Johannes Weiner <hannes@cmpxchg.org>
    Cc: Suren Baghdasaryan <surenb@google.com>
    Cc: Zi Yan <ziy@nvidia.com>
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f5ee7c0b5841a3dbe1bcf46c8f663c67d3d3edf4
Author: Lance Yang <lance.yang@linux.dev>
Date:   Tue Sep 30 16:10:40 2025 +0800

    mm/rmap: fix soft-dirty and uffd-wp bit loss when remapping zero-filled mTHP subpage to shared zeropage
    
    commit 9658d698a8a83540bf6a6c80d13c9a61590ee985 upstream.
    
    When splitting an mTHP and replacing a zero-filled subpage with the shared
    zeropage, try_to_map_unused_to_zeropage() currently drops several
    important PTE bits.
    
    For userspace tools like CRIU, which rely on the soft-dirty mechanism for
    incremental snapshots, losing the soft-dirty bit means modified pages are
    missed, leading to inconsistent memory state after restore.
    
    As pointed out by David, the more critical uffd-wp bit is also dropped.
    This breaks the userfaultfd write-protection mechanism, causing writes to
    be silently missed by monitoring applications, which can lead to data
    corruption.
    
    Preserve both the soft-dirty and uffd-wp bits from the old PTE when
    creating the new zeropage mapping to ensure they are correctly tracked.
    
    Link: https://lkml.kernel.org/r/20250930081040.80926-1-lance.yang@linux.dev
    Fixes: b1f202060afe ("mm: remap unused subpages to shared zeropage when splitting isolated thp")
    Signed-off-by: Lance Yang <lance.yang@linux.dev>
    Suggested-by: David Hildenbrand <david@redhat.com>
    Suggested-by: Dev Jain <dev.jain@arm.com>
    Acked-by: David Hildenbrand <david@redhat.com>
    Reviewed-by: Dev Jain <dev.jain@arm.com>
    Acked-by: Zi Yan <ziy@nvidia.com>
    Reviewed-by: Liam R. Howlett <Liam.Howlett@oracle.com>
    Reviewed-by: Harry Yoo <harry.yoo@oracle.com>
    Cc: Alistair Popple <apopple@nvidia.com>
    Cc: Baolin Wang <baolin.wang@linux.alibaba.com>
    Cc: Barry Song <baohua@kernel.org>
    Cc: Byungchul Park <byungchul@sk.com>
    Cc: Gregory Price <gourry@gourry.net>
    Cc: "Huang, Ying" <ying.huang@linux.alibaba.com>
    Cc: Jann Horn <jannh@google.com>
    Cc: Joshua Hahn <joshua.hahnjy@gmail.com>
    Cc: Lorenzo Stoakes <lorenzo.stoakes@oracle.com>
    Cc: Mariano Pache <npache@redhat.com>
    Cc: Mathew Brost <matthew.brost@intel.com>
    Cc: Peter Xu <peterx@redhat.com>
    Cc: Rakie Kim <rakie.kim@sk.com>
    Cc: Rik van Riel <riel@surriel.com>
    Cc: Ryan Roberts <ryan.roberts@arm.com>
    Cc: Usama Arif <usamaarif642@gmail.com>
    Cc: Vlastimil Babka <vbabka@suse.cz>
    Cc: Yu Zhao <yuzhao@google.com>
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 78da3fae20aa2b71cfc0e50a37fe100eb6aee890
Author: Lance Yang <lance.yang@linux.dev>
Date:   Mon Sep 22 10:14:58 2025 +0800

    mm/thp: fix MTE tag mismatch when replacing zero-filled subpages
    
    commit 1ce6473d17e78e3cb9a40147658231731a551828 upstream.
    
    When both THP and MTE are enabled, splitting a THP and replacing its
    zero-filled subpages with the shared zeropage can cause MTE tag mismatch
    faults in userspace.
    
    Remapping zero-filled subpages to the shared zeropage is unsafe, as the
    zeropage has a fixed tag of zero, which may not match the tag expected by
    the userspace pointer.
    
    KSM already avoids this problem by using memcmp_pages(), which on arm64
    intentionally reports MTE-tagged pages as non-identical to prevent unsafe
    merging.
    
    As suggested by David[1], this patch adopts the same pattern, replacing the
    memchr_inv() byte-level check with a call to pages_identical(). This
    leverages existing architecture-specific logic to determine if a page is
    truly identical to the shared zeropage.
    
    Having both the THP shrinker and KSM rely on pages_identical() makes the
    design more future-proof, IMO. Instead of handling quirks in generic code,
    we just let the architecture decide what makes two pages identical.
    
    [1] https://lore.kernel.org/all/ca2106a3-4bb2-4457-81af-301fd99fbef4@redhat.com
    
    Link: https://lkml.kernel.org/r/20250922021458.68123-1-lance.yang@linux.dev
    Fixes: b1f202060afe ("mm: remap unused subpages to shared zeropage when splitting isolated thp")
    Signed-off-by: Lance Yang <lance.yang@linux.dev>
    Reported-by: Qun-wei Lin <Qun-wei.Lin@mediatek.com>
    Closes: https://lore.kernel.org/all/a7944523fcc3634607691c35311a5d59d1a3f8d4.camel@mediatek.com
    Suggested-by: David Hildenbrand <david@redhat.com>
    Acked-by: Zi Yan <ziy@nvidia.com>
    Acked-by: David Hildenbrand <david@redhat.com>
    Acked-by: Usama Arif <usamaarif642@gmail.com>
    Reviewed-by: Catalin Marinas <catalin.marinas@arm.com>
    Reviewed-by: Wei Yang <richard.weiyang@gmail.com>
    Cc: Alistair Popple <apopple@nvidia.com>
    Cc: andrew.yang <andrew.yang@mediatek.com>
    Cc: Baolin Wang <baolin.wang@linux.alibaba.com>
    Cc: Barry Song <baohua@kernel.org>
    Cc: Byungchul Park <byungchul@sk.com>
    Cc: Charlie Jenkins <charlie@rivosinc.com>
    Cc: Chinwen Chang <chinwen.chang@mediatek.com>
    Cc: Dev Jain <dev.jain@arm.com>
    Cc: Domenico Cerasuolo <cerasuolodomenico@gmail.com>
    Cc: Gregory Price <gourry@gourry.net>
    Cc: "Huang, Ying" <ying.huang@linux.alibaba.com>
    Cc: Hugh Dickins <hughd@google.com>
    Cc: Johannes Weiner <hannes@cmpxchg.org>
    Cc: Joshua Hahn <joshua.hahnjy@gmail.com>
    Cc: Kairui Song <ryncsn@gmail.com>
    Cc: Kalesh Singh <kaleshsingh@google.com>
    Cc: Liam Howlett <liam.howlett@oracle.com>
    Cc: Lorenzo Stoakes <lorenzo.stoakes@oracle.com>
    Cc: Mariano Pache <npache@redhat.com>
    Cc: Mathew Brost <matthew.brost@intel.com>
    Cc: Matthew Wilcox (Oracle) <willy@infradead.org>
    Cc: Mike Rapoport <rppt@kernel.org>
    Cc: Palmer Dabbelt <palmer@rivosinc.com>
    Cc: Rakie Kim <rakie.kim@sk.com>
    Cc: Rik van Riel <riel@surriel.com>
    Cc: Roman Gushchin <roman.gushchin@linux.dev>
    Cc: Ryan Roberts <ryan.roberts@arm.com>
    Cc: Samuel Holland <samuel.holland@sifive.com>
    Cc: Shakeel Butt <shakeel.butt@linux.dev>
    Cc: Suren Baghdasaryan <surenb@google.com>
    Cc: Yu Zhao <yuzhao@google.com>
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 1a4b0c26e1b0472153564d3bf5e893929f317b8b
Author: Nick Morrow <morrownr@gmail.com>
Date:   Fri Sep 12 15:45:56 2025 -0500

    wifi: mt76: mt7921u: Add VID/PID for Netgear A7500
    
    commit fc6627ca8a5f811b601aea74e934cf8a048c88ac upstream.
    
    Add VID/PID 0846/9065 for Netgear A7500.
    
    Reported-by: Autumn Dececco <autumndececco@gmail.com>
    Tested-by: Autumn Dececco <autumndececco@gmail.com>
    Signed-off-by: Nick Morrow <morrownr@gmail.com>
    Cc: stable@vger.kernel.org
    Acked-by: Lorenzo Bianconi <lorenzo@kernel.org>
    Link: https://patch.msgid.link/80bacfd6-6073-4ce5-be32-ae9580832337@gmail.com
    Signed-off-by: Felix Fietkau <nbd@nbd.name>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 34a7b7a4c1eb9853bc02e93bcd6c371d2c72189b
Author: Nick Morrow <morrownr@gmail.com>
Date:   Tue Jul 8 16:40:42 2025 -0500

    wifi: mt76: mt7925u: Add VID/PID for Netgear A9000
    
    commit f6159b2051e157550d7609e19d04471609c6050b upstream.
    
    Add VID/PID 0846/9072 for recently released Netgear A9000.
    
    Signed-off-by: Nick Morrow <morrownr@gmail.com>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/7afd3c3c-e7cf-4bd9-801d-bdfc76def506@gmail.com
    Signed-off-by: Felix Fietkau <nbd@nbd.name>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit b5204956ab74c1139dc33d9754e2ea0714d01f01
Author: Fedor Pchelkin <pchelkin@ispras.ru>
Date:   Sat Sep 20 00:08:48 2025 +0300

    wifi: rtw89: avoid possible TX wait initialization race
    
    commit c24248ed78f33ea299ea61d105355ba47157d49f upstream.
    
    The value of skb_data->wait indicates whether skb is passed on to the
    core mac80211 stack or released by the driver itself.  Make sure that by
    the time skb is added to txwd queue and becomes visible to the completing
    side, it has already allocated and initialized TX wait related data (in
    case it's needed).
    
    This is found by code review and addresses a possible race scenario
    described below:
    
          Waiting thread                          Completing thread
    
    rtw89_core_send_nullfunc()
      rtw89_core_tx_write_link()
        ...
        rtw89_pci_txwd_submit()
          skb_data->wait = NULL
          /* add skb to the queue */
          skb_queue_tail(&txwd->queue, skb)
    
      /* another thread (e.g. rtw89_ops_tx) performs TX kick off for the same queue */
    
                                                rtw89_pci_napi_poll()
                                                ...
                                                  rtw89_pci_release_txwd_skb()
                                                    /* get skb from the queue */
                                                    skb_unlink(skb, &txwd->queue)
                                                    rtw89_pci_tx_status()
                                                      rtw89_core_tx_wait_complete()
                                                      /* use incorrect skb_data->wait */
      rtw89_core_tx_kick_off_and_wait()
      /* assign skb_data->wait but too late */
    
    Found by Linux Verification Center (linuxtesting.org).
    
    Fixes: 1ae5ca615285 ("wifi: rtw89: add function to wait for completion of TX skbs")
    Cc: stable@vger.kernel.org
    Signed-off-by: Fedor Pchelkin <pchelkin@ispras.ru>
    Acked-by: Ping-Ke Shih <pkshih@realtek.com>
    Signed-off-by: Ping-Ke Shih <pkshih@realtek.com>
    Link: https://patch.msgid.link/20250919210852.823912-3-pchelkin@ispras.ru
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 15b31e8b87fd1d57bfc0f2f8cacc1d0e9dbdc90d
Author: Miaoqian Lin <linmq006@gmail.com>
Date:   Tue Sep 2 12:09:49 2025 +0800

    wifi: iwlwifi: Fix dentry reference leak in iwl_mld_add_link_debugfs
    
    commit ff46e2e7034c78489fa7a6bc35f7c9dd8ab82905 upstream.
    
    The debugfs_lookup() function increases the dentry reference count.
    Add missing dput() call to release the reference when the "iwlmld"
    directory already exists.
    
    Fixes: d1e879ec600f ("wifi: iwlwifi: add iwlmld sub-driver")
    Cc: stable@vger.kernel.org
    Signed-off-by: Miaoqian Lin <linmq006@gmail.com>
    Link: https://patch.msgid.link/20250902040955.2362472-1-linmq006@gmail.com
    Signed-off-by: Miri Korenblit <miriam.rachel.korenblit@intel.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 79266fd78df15585e2fd6c9b8a0ee122749a4b77
Author: Muhammad Usama Anjum <usama.anjum@collabora.com>
Date:   Tue Jul 22 10:31:21 2025 +0500

    wifi: ath11k: HAL SRNG: don't deinitialize and re-initialize again
    
    commit 32be3ca4cf78b309dfe7ba52fe2d7cc3c23c5634 upstream.
    
    Don't deinitialize and reinitialize the HAL helpers. The dma memory is
    deallocated and there is high possibility that we'll not be able to get
    the same memory allocated from dma when there is high memory pressure.
    
    Tested-on: WCN6855 hw2.0 PCI WLAN.HSP.1.1-03926.13-QCAHSPSWPL_V2_SILICONZ_CE-2.52297.6
    
    Fixes: d5c65159f289 ("ath11k: driver for Qualcomm IEEE 802.11ax devices")
    Cc: stable@vger.kernel.org
    Cc: Baochen Qiang <baochen.qiang@oss.qualcomm.com>
    Reviewed-by: Baochen Qiang <baochen.qiang@oss.qualcomm.com>
    Signed-off-by: Muhammad Usama Anjum <usama.anjum@collabora.com>
    Link: https://patch.msgid.link/20250722053121.1145001-1-usama.anjum@collabora.com
    Signed-off-by: Jeff Johnson <jeff.johnson@oss.qualcomm.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 07e38a54cabd9b4de7ceb7f075f29ffa463e458a
Author: Suren Baghdasaryan <surenb@google.com>
Date:   Mon Sep 15 13:09:18 2025 -0700

    slab: mark slab->obj_exts allocation failures unconditionally
    
    commit f7381b9116407ba2a429977c80ff8df953ea9354 upstream.
    
    alloc_slab_obj_exts() should mark failed obj_exts vector allocations
    independent on whether the vector is being allocated for a new or an
    existing slab. Current implementation skips doing this for existing
    slabs. Fix this by marking failed allocations unconditionally.
    
    Fixes: 09c46563ff6d ("codetag: debug: introduce OBJEXTS_ALLOC_FAIL to mark failed slab_ext allocations")
    Reported-by: Shakeel Butt <shakeel.butt@linux.dev>
    Closes: https://lore.kernel.org/all/avhakjldsgczmq356gkwmvfilyvf7o6temvcmtt5lqd4fhp5rk@47gp2ropyixg/
    Signed-off-by: Suren Baghdasaryan <surenb@google.com>
    Cc: stable@vger.kernel.org # v6.10+
    Acked-by: Shakeel Butt <shakeel.butt@linux.dev>
    Signed-off-by: Vlastimil Babka <vbabka@suse.cz>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 51aa14cad3b66ebf5a199c76808c45c7e6c3a24d
Author: Suren Baghdasaryan <surenb@google.com>
Date:   Mon Sep 15 13:09:17 2025 -0700

    slab: prevent warnings when slab obj_exts vector allocation fails
    
    commit 4038016397da5c1cebb10e7c85a36d06123724a8 upstream.
    
    When object extension vector allocation fails, we set slab->obj_exts to
    OBJEXTS_ALLOC_FAIL to indicate the failure. Later, once the vector is
    successfully allocated, we will use this flag to mark codetag references
    stored in that vector as empty to avoid codetag warnings.
    
    slab_obj_exts() used to retrieve the slab->obj_exts vector pointer checks
    slab->obj_exts for being either NULL or a pointer with MEMCG_DATA_OBJEXTS
    bit set. However it does not handle the case when slab->obj_exts equals
    OBJEXTS_ALLOC_FAIL. Add the missing condition to avoid extra warning.
    
    Fixes: 09c46563ff6d ("codetag: debug: introduce OBJEXTS_ALLOC_FAIL to mark failed slab_ext allocations")
    Reported-by: Shakeel Butt <shakeel.butt@linux.dev>
    Closes: https://lore.kernel.org/all/jftidhymri2af5u3xtcqry3cfu6aqzte3uzlznhlaylgrdztsi@5vpjnzpsemf5/
    Signed-off-by: Suren Baghdasaryan <surenb@google.com>
    Cc: stable@vger.kernel.org # v6.10+
    Acked-by: Shakeel Butt <shakeel.butt@linux.dev>
    Signed-off-by: Vlastimil Babka <vbabka@suse.cz>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 2d1427dd6f8417737079ccf1ed444a3056cfb94c
Author: Heiko Carstens <hca@linux.ibm.com>
Date:   Fri Sep 26 15:39:10 2025 +0200

    s390: Add -Wno-pointer-sign to KBUILD_CFLAGS_DECOMPRESSOR
    
    commit fa7a0a53eeb7e16402f82c3d5a9ef4bf5efe9357 upstream.
    
    If the decompressor is compiled with clang this can lead to the following
    warning:
    
    In file included from arch/s390/boot/startup.c:4:
    ...
    In file included from ./include/linux/pgtable.h:6:
    ./arch/s390/include/asm/pgtable.h:2065:48: warning: passing 'unsigned long *' to parameter of type
          'long *' converts between pointers to integer types with different sign [-Wpointer-sign]
     2065 |                 value = __atomic64_or_barrier(PGSTE_PCL_BIT, ptr);
    
    Add -Wno-pointer-sign to the decompressor compile flags, like it is also
    done for the kernel. This is similar to what was done for x86 to address
    the same problem [1].
    
    [1] commit dca5203e3fe2 ("x86/boot: Add -Wno-pointer-sign to KBUILD_CFLAGS")
    
    Cc: stable@vger.kernel.org
    Reported-by: Gerd Bayer <gbayer@linux.ibm.com>
    Signed-off-by: Heiko Carstens <hca@linux.ibm.com>
    Reviewed-by: Alexander Gordeev <agordeev@linux.ibm.com>
    Signed-off-by: Alexander Gordeev <agordeev@linux.ibm.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f84f57b777359d859f11a7c9be0cef4e36fb5094
Author: Jaehoon Kim <jhkim@linux.ibm.com>
Date:   Thu Sep 25 17:47:07 2025 +0200

    s390/dasd: Return BLK_STS_INVAL for EINVAL from do_dasd_request
    
    commit 8f4ed0ce4857ceb444174503fc9058720d4faaa1 upstream.
    
    Currently, if CCW request creation fails with -EINVAL, the DASD driver
    returns BLK_STS_IOERR to the block layer.
    
    This can happen, for example, when a user-space application such as QEMU
    passes a misaligned buffer, but the original cause of the error is
    masked as a generic I/O error.
    
    This patch changes the behavior so that -EINVAL is returned as
    BLK_STS_INVAL, allowing user space to properly detect alignment issues
    instead of interpreting them as I/O errors.
    
    Reviewed-by: Stefan Haberland <sth@linux.ibm.com>
    Cc: stable@vger.kernel.org #6.11+
    Signed-off-by: Jaehoon Kim <jhkim@linux.ibm.com>
    Signed-off-by: Stefan Haberland <sth@linux.ibm.com>
    Signed-off-by: Jens Axboe <axboe@kernel.dk>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 4e6f98bf23cde3635ed3b63a8c65eb4b2ae79d55
Author: Jaehoon Kim <jhkim@linux.ibm.com>
Date:   Thu Sep 25 17:47:08 2025 +0200

    s390/dasd: enforce dma_alignment to ensure proper buffer validation
    
    commit 130e6de62107116eba124647116276266be0f84c upstream.
    
    The block layer validates buffer alignment using the device's
    dma_alignment value. If dma_alignment is smaller than
    logical_block_size(bp_block) -1, misaligned buffer incorrectly pass
    validation and propagate to the lower-level driver.
    
    This patch adjusts dma_alignment to be at least logical_block_size -1,
    ensuring that misalignment buffers are properly rejected at the block
    layer and do not reach the DASD driver unnecessarily.
    
    Fixes: 2a07bb64d801 ("s390/dasd: Remove DMA alignment")
    Reviewed-by: Stefan Haberland <sth@linux.ibm.com>
    Cc: stable@vger.kernel.org #6.11+
    Signed-off-by: Jaehoon Kim <jhkim@linux.ibm.com>
    Signed-off-by: Stefan Haberland <sth@linux.ibm.com>
    Signed-off-by: Jens Axboe <axboe@kernel.dk>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 0a50182e6a94f670ea1b106d68ef74c18bb81100
Author: Heiko Carstens <hca@linux.ibm.com>
Date:   Thu Sep 25 10:45:17 2025 +0200

    s390/cio/ioasm: Fix __xsch() condition code handling
    
    commit f0edc8f113a39d1c9f8cf83e865c32b0668d80e0 upstream.
    
    For the __xsch() inline assembly the conversion to flag output macros is
    incomplete. Only the conditional shift of the return value was added, while
    the required changes to the inline assembly itself are missing.
    
    If compiled with GCC versions before 14.2 this leads to a double shift of
    the cc output operand and therefore the returned value of __xsch() is
    incorrectly always zero, instead of the expected condition code.
    
    Fixes: e200565d434b ("s390/cio/ioasm: Convert to use flag output macros")
    Cc: stable@vger.kernel.org
    Signed-off-by: Heiko Carstens <hca@linux.ibm.com>
    Acked-by: Alexander Gordeev <agordeev@linux.ibm.com>
    Reviewed-by: Juergen Christ <jchrist@linux.ibm.com>
    Signed-off-by: Alexander Gordeev <agordeev@linux.ibm.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit c5117131b4b688541801720a13baf4f58cff4e20
Author: Matthieu Baerts (NGI0) <matttbe@kernel.org>
Date:   Thu Sep 25 12:32:37 2025 +0200

    selftests: mptcp: join: validate C-flag + def limit
    
    commit 008385efd05e04d8dff299382df2e8be0f91d8a0 upstream.
    
    The previous commit adds an exception for the C-flag case. The
    'mptcp_join.sh' selftest is extended to validate this case.
    
    In this subtest, there is a typical CDN deployment with a client where
    MPTCP endpoints have been 'automatically' configured:
    
    - the server set net.mptcp.allow_join_initial_addr_port=0
    
    - the client has multiple 'subflow' endpoints, and the default limits:
      not accepting ADD_ADDRs.
    
    Without the parent patch, the client is not able to establish new
    subflows using its 'subflow' endpoints. The parent commit fixes that.
    
    The 'Fixes' tag here below is the same as the one from the previous
    commit: this patch here is not fixing anything wrong in the selftests,
    but it validates the previous fix for an issue introduced by this commit
    ID.
    
    Fixes: df377be38725 ("mptcp: add deny_join_id0 in mptcp_options_received")
    Cc: stable@vger.kernel.org
    Reviewed-by: Geliang Tang <geliang@kernel.org>
    Signed-off-by: Matthieu Baerts (NGI0) <matttbe@kernel.org>
    Link: https://patch.msgid.link/20250925-net-next-mptcp-c-flag-laminar-v1-2-ad126cc47c6b@kernel.org
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 461d135c70bc6f05236d4f76a4d6f430be7525d4
Author: Matthieu Baerts (NGI0) <matttbe@kernel.org>
Date:   Thu Sep 18 10:50:18 2025 +0200

    mptcp: reset blackhole on success with non-loopback ifaces
    
    commit 833d4313bc1e9e194814917d23e8874d6b651649 upstream.
    
    When a first MPTCP connection gets successfully established after a
    blackhole period, 'active_disable_times' was supposed to be reset when
    this connection was done via any non-loopback interfaces.
    
    Unfortunately, the opposite condition was checked: only reset when the
    connection was established via a loopback interface. Fixing this by
    simply looking at the opposite.
    
    This is similar to what is done with TCP FastOpen, see
    tcp_fastopen_active_disable_ofo_check().
    
    This patch is a follow-up of a previous discussion linked to commit
    893c49a78d9f ("mptcp: Use __sk_dst_get() and dst_dev_rcu() in
    mptcp_active_enable()."), see [1].
    
    Fixes: 27069e7cb3d1 ("mptcp: disable active MPTCP in case of blackhole")
    Cc: stable@vger.kernel.org
    Link: https://lore.kernel.org/4209a283-8822-47bd-95b7-87e96d9b7ea3@kernel.org [1]
    Signed-off-by: Matthieu Baerts (NGI0) <matttbe@kernel.org>
    Reviewed-by: Simon Horman <horms@kernel.org>
    Reviewed-by: Kuniyuki Iwashima <kuniyu@google.com>
    Link: https://patch.msgid.link/20250918-net-next-mptcp-blackhole-reset-loopback-v1-1-bf5818326639@kernel.org
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 8b603e8068918f3afe260cf81e45805b8857cb5c
Author: Matthieu Baerts (NGI0) <matttbe@kernel.org>
Date:   Thu Sep 25 12:32:36 2025 +0200

    mptcp: pm: in-kernel: usable client side with C-flag
    
    commit 4b1ff850e0c1aacc23e923ed22989b827b9808f9 upstream.
    
    When servers set the C-flag in their MP_CAPABLE to tell clients not to
    create subflows to the initial address and port, clients will likely not
    use their other endpoints. That's because the in-kernel path-manager
    uses the 'subflow' endpoints to create subflows only to the initial
    address and port.
    
    If the limits have not been modified to accept ADD_ADDR, the client
    doesn't try to establish new subflows. If the limits accept ADD_ADDR,
    the routing routes will be used to select the source IP.
    
    The C-flag is typically set when the server is operating behind a legacy
    Layer 4 load balancer, or using anycast IP address. Clients having their
    different 'subflow' endpoints setup, don't end up creating multiple
    subflows as expected, and causing some deployment issues.
    
    A special case is then added here: when servers set the C-flag in the
    MPC and directly sends an ADD_ADDR, this single ADD_ADDR is accepted.
    The 'subflows' endpoints will then be used with this new remote IP and
    port. This exception is only allowed when the ADD_ADDR is sent
    immediately after the 3WHS, and makes the client switching to the 'fully
    established' mode. After that, 'select_local_address()' will not be able
    to find any subflows, because 'id_avail_bitmap' will be filled in
    mptcp_pm_create_subflow_or_signal_addr(), when switching to 'fully
    established' mode.
    
    Fixes: df377be38725 ("mptcp: add deny_join_id0 in mptcp_options_received")
    Cc: stable@vger.kernel.org
    Closes: https://github.com/multipath-tcp/mptcp_net-next/issues/536
    Reviewed-by: Geliang Tang <geliang@kernel.org>
    Signed-off-by: Matthieu Baerts (NGI0) <matttbe@kernel.org>
    Link: https://patch.msgid.link/20250925-net-next-mptcp-c-flag-laminar-v1-1-ad126cc47c6b@kernel.org
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 703023de2fdd3fedb0b86b29a268a714376932c7
Author: Sean Christopherson <seanjc@google.com>
Date:   Fri Aug 8 10:23:57 2025 -0700

    x86/umip: Fix decoding of register forms of 0F 01 (SGDT and SIDT aliases)
    
    commit 27b1fd62012dfe9d3eb8ecde344d7aa673695ecf upstream.
    
    Filter out the register forms of 0F 01 when determining whether or not to
    emulate in response to a potential UMIP violation #GP, as SGDT and SIDT only
    accept memory operands.  The register variants of 0F 01 are used to encode
    instructions for things like VMX and SGX, i.e. not checking the Mod field
    would cause the kernel to incorrectly emulate on #GP, e.g. due to a CPL
    violation on VMLAUNCH.
    
    Fixes: 1e5db223696a ("x86/umip: Add emulation code for UMIP instructions")
    Signed-off-by: Sean Christopherson <seanjc@google.com>
    Signed-off-by: Borislav Petkov (AMD) <bp@alien8.de>
    Acked-by: Peter Zijlstra (Intel) <peterz@infradead.org>
    Cc: stable@vger.kernel.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f2e4b19e2c84418349fed4c8dcbbcdb77f5e8233
Author: Sean Christopherson <seanjc@google.com>
Date:   Fri Aug 8 10:23:56 2025 -0700

    x86/umip: Check that the instruction opcode is at least two bytes
    
    commit 32278c677947ae2f042c9535674a7fff9a245dd3 upstream.
    
    When checking for a potential UMIP violation on #GP, verify the decoder found
    at least two opcode bytes to avoid false positives when the kernel encounters
    an unknown instruction that starts with 0f.  Because the array of opcode.bytes
    is zero-initialized by insn_init(), peeking at bytes[1] will misinterpret
    garbage as a potential SLDT or STR instruction, and can incorrectly trigger
    emulation.
    
    E.g. if a VPALIGNR instruction
    
       62 83 c5 05 0f 08 ff     vpalignr xmm17{k5},xmm23,XMMWORD PTR [r8],0xff
    
    hits a #GP, the kernel emulates it as STR and squashes the #GP (and corrupts
    the userspace code stream).
    
    Arguably the check should look for exactly two bytes, but no three byte
    opcodes use '0f 00 xx' or '0f 01 xx' as an escape, i.e. it should be
    impossible to get a false positive if the first two opcode bytes match '0f 00'
    or '0f 01'.  Go with a more conservative check with respect to the existing
    code to minimize the chances of breaking userspace, e.g. due to decoder
    weirdness.
    
    Analyzed by Nick Bray <ncbray@google.com>.
    
    Fixes: 1e5db223696a ("x86/umip: Add emulation code for UMIP instructions")
    Reported-by: Dan Snyder <dansnyder@google.com>
    Signed-off-by: Sean Christopherson <seanjc@google.com>
    Signed-off-by: Borislav Petkov (AMD) <bp@alien8.de>
    Acked-by: Peter Zijlstra (Intel) <peterz@infradead.org>
    Cc: stable@vger.kernel.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit acc2b118c51417f06062c9c61f720362eeea8da1
Author: Xin Li (Intel) <xin@zytor.com>
Date:   Tue Jul 15 23:33:20 2025 -0700

    x86/fred: Remove ENDBR64 from FRED entry points
    
    commit 3da01ffe1aeaa0d427ab5235ba735226670a80d9 upstream.
    
    The FRED specification has been changed in v9.0 to state that there
    is no need for FRED event handlers to begin with ENDBR64, because
    in the presence of supervisor indirect branch tracking, FRED event
    delivery does not enter the WAIT_FOR_ENDBRANCH state.
    
    As a result, remove ENDBR64 from FRED entry points.
    
    Then add ANNOTATE_NOENDBR to indicate that FRED entry points will
    never be used for indirect calls to suppress an objtool warning.
    
    This change implies that any indirect CALL/JMP to FRED entry points
    causes #CP in the presence of supervisor indirect branch tracking.
    
    Credit goes to Jennifer Miller <jmill@asu.edu> and other contributors
    from Arizona State University whose research shows that placing ENDBR
    at entry points has negative value thus led to this change.
    
    Note: This is obviously an incompatible change to the FRED
    architecture.  But, it's OK because there no FRED systems out in the
    wild today. All production hardware and late pre-production hardware
    will follow the FRED v9 spec and be compatible with this approach.
    
    [ dhansen: add note to changelog about incompatibility ]
    
    Fixes: 14619d912b65 ("x86/fred: FRED entry/exit and dispatch code")
    Signed-off-by: Xin Li (Intel) <xin@zytor.com>
    Signed-off-by: Dave Hansen <dave.hansen@linux.intel.com>
    Reviewed-by: H. Peter Anvin (Intel) <hpa@zytor.com>
    Reviewed-by: Andrew Cooper <andrew.cooper3@citrix.com>
    Link: https://lore.kernel.org/linux-hardening/Z60NwR4w%2F28Z7XUa@ubun/
    Cc:stable@vger.kernel.org
    Link: https://lore.kernel.org/all/20250716063320.1337818-1-xin%40zytor.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit d633455d9826acd980b44c5669f9a30611e80a21
Author: Darrick J. Wong <djwong@kernel.org>
Date:   Tue Apr 8 16:14:32 2025 -0700

    xfs: use deferred intent items for reaping crosslinked blocks
    
    commit cd32a0c0dcdf634f2e0e71f41c272e19dece6264 upstream.
    
    When we're removing rmap records for crosslinked blocks, use deferred
    intent items so that we can try to free/unmap as many of the old data
    structure's blocks as we can in the same transaction as the commit.
    
    Cc: <stable@vger.kernel.org> # v6.6
    Fixes: 1c7ce115e52106 ("xfs: reap large AG metadata extents when possible")
    Signed-off-by: "Darrick J. Wong" <djwong@kernel.org>
    Reviewed-by: Christoph Hellwig <hch@lst.de>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f16252636b9f164d798b4b1aff6ce4973e2ee708
Author: Santhosh Kumar K <s-k6@ti.com>
Date:   Sat Sep 6 00:29:57 2025 +0530

    spi: cadence-quadspi: Fix cqspi_setup_flash()
    
    commit 858d4d9e0a9d6b64160ef3c824f428c9742172c4 upstream.
    
    The 'max_cs' stores the largest chip select number. It should only
    be updated when the current 'cs' is greater than existing 'max_cs'. So,
    fix the condition accordingly.
    
    Also, return failure if there are no flash device declared.
    
    Fixes: 0f3841a5e115 ("spi: cadence-qspi: report correct number of chip-select")
    CC: stable@vger.kernel.org
    Reviewed-by: Pratyush Yadav <pratyush@kernel.org>
    Reviewed-by: Théo Lebrun <theo.lebrun@bootlin.com>
    Signed-off-by: Santhosh Kumar K <s-k6@ti.com>
    Message-ID: <20250905185958.3575037-4-s-k6@ti.com>
    Signed-off-by: Mark Brown <broonie@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit d36b5d98922e6eecd7dc6f6237d8d70585d6a689
Author: Pratyush Yadav <pratyush@kernel.org>
Date:   Sat Sep 6 00:29:56 2025 +0530

    spi: cadence-quadspi: Flush posted register writes before DAC access
    
    commit 1ad55767e77a853c98752ed1e33b68049a243bd7 upstream.
    
    cqspi_read_setup() and cqspi_write_setup() program the address width as
    the last step in the setup. This is likely to be immediately followed by
    a DAC region read/write. On TI K3 SoCs the DAC region is on a different
    endpoint from the register region. This means that the order of the two
    operations is not guaranteed, and they might be reordered at the
    interconnect level. It is possible that the DAC read/write goes through
    before the address width update goes through. In this situation if the
    previous command used a different address width the OSPI command is sent
    with the wrong number of address bytes, resulting in an invalid command
    and undefined behavior.
    
    Read back the size register to make sure the write gets flushed before
    accessing the DAC region.
    
    Fixes: 140623410536 ("mtd: spi-nor: Add driver for Cadence Quad SPI Flash Controller")
    CC: stable@vger.kernel.org
    Reviewed-by: Pratyush Yadav <pratyush@kernel.org>
    Signed-off-by: Pratyush Yadav <pratyush@kernel.org>
    Signed-off-by: Santhosh Kumar K <s-k6@ti.com>
    Message-ID: <20250905185958.3575037-3-s-k6@ti.com>
    Signed-off-by: Mark Brown <broonie@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit c4a255a19127d94a11a195b81ead2c8eab3d2dd0
Author: Pratyush Yadav <pratyush@kernel.org>
Date:   Sat Sep 6 00:29:55 2025 +0530

    spi: cadence-quadspi: Flush posted register writes before INDAC access
    
    commit 29e0b471ccbd674d20d4bbddea1a51e7105212c5 upstream.
    
    cqspi_indirect_read_execute() and cqspi_indirect_write_execute() first
    set the enable bit on APB region and then start reading/writing to the
    AHB region. On TI K3 SoCs these regions lie on different endpoints. This
    means that the order of the two operations is not guaranteed, and they
    might be reordered at the interconnect level.
    
    It is possible for the AHB write to be executed before the APB write to
    enable the indirect controller, causing the transaction to be invalid
    and the write erroring out. Read back the APB region write before
    accessing the AHB region to make sure the write got flushed and the race
    condition is eliminated.
    
    Fixes: 140623410536 ("mtd: spi-nor: Add driver for Cadence Quad SPI Flash Controller")
    CC: stable@vger.kernel.org
    Reviewed-by: Pratyush Yadav <pratyush@kernel.org>
    Signed-off-by: Pratyush Yadav <pratyush@kernel.org>
    Signed-off-by: Santhosh Kumar K <s-k6@ti.com>
    Message-ID: <20250905185958.3575037-2-s-k6@ti.com>
    Signed-off-by: Mark Brown <broonie@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f839e90ecc922d486a12df96853eaddad52450d3
Author: Johan Hovold <johan+linaro@kernel.org>
Date:   Mon Jul 21 17:36:09 2025 +0200

    PCI/pwrctrl: Fix device leak at device stop
    
    commit dc32e9346b26ba33e84ec3034a1e53a9733700f9 upstream.
    
    Make sure to drop the reference to the pwrctrl device taken by
    of_find_device_by_node() when stopping a PCI device.
    
    Fixes: 681725afb6b9 ("PCI/pwrctl: Remove pwrctl device without iterating over all children of pwrctl parent")
    Signed-off-by: Johan Hovold <johan+linaro@kernel.org>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Reviewed-by: Manivannan Sadhasivam <mani@kernel.org>
    Cc: stable@vger.kernel.org      # v6.13
    Link: https://patch.msgid.link/20250721153609.8611-4-johan+linaro@kernel.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a5053388f5ebe77f727f7c33f5783a198fe10a09
Author: Johan Hovold <johan+linaro@kernel.org>
Date:   Mon Jul 21 17:36:08 2025 +0200

    PCI/pwrctrl: Fix device and OF node leak at bus scan
    
    commit e24bbbe0780262a21fc8619fe99078a5b8d64b18 upstream.
    
    Make sure to drop the references to the pwrctrl OF node and device taken by
    of_pci_find_child_device() and of_find_device_by_node() respectively when
    scanning the bus.
    
    Fixes: 957f40d039a9 ("PCI/pwrctrl: Move creation of pwrctrl devices to pci_scan_device()")
    Signed-off-by: Johan Hovold <johan+linaro@kernel.org>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Reviewed-by: Manivannan Sadhasivam <mani@kernel.org>
    Cc: stable@vger.kernel.org      # v6.15
    Link: https://patch.msgid.link/20250721153609.8611-3-johan+linaro@kernel.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit fac1874e94cd6970acdd574c03b88584b57c3c3e
Author: Johan Hovold <johan+linaro@kernel.org>
Date:   Mon Jul 21 17:36:07 2025 +0200

    PCI/pwrctrl: Fix device leak at registration
    
    commit 39f9be6aba3ae4d6fdd4b8554f1184d054d7a713 upstream.
    
    Make sure to drop the reference to the pwrctrl device taken by
    of_find_device_by_node() when registering a PCI device.
    
    Fixes: b458ff7e8176 ("PCI/pwrctl: Ensure that pwrctl drivers are probed before PCI client drivers")
    Signed-off-by: Johan Hovold <johan+linaro@kernel.org>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Reviewed-by: Manivannan Sadhasivam <mani@kernel.org>
    Cc: stable@vger.kernel.org      # v6.13
    Link: https://patch.msgid.link/20250721153609.8611-2-johan+linaro@kernel.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 35ae4e321fe1bd1ab2f3fe114f68c7bfc3ba3894
Author: Niklas Cassel <cassel@kernel.org>
Date:   Mon Sep 22 16:08:25 2025 +0200

    PCI: tegra194: Reset BARs when running in PCIe endpoint mode
    
    commit 42f9c66a6d0cc45758dab77233c5460e1cf003df upstream.
    
    Tegra already defines all BARs except BAR0 as BAR_RESERVED.  This is
    sufficient for pci-epf-test to not allocate backing memory and to not call
    set_bar() for those BARs. However, marking a BAR as BAR_RESERVED does not
    mean that the BAR gets disabled.
    
    The host side driver, pci_endpoint_test, simply does an ioremap for all
    enabled BARs and will run tests against all enabled BARs, so it will run
    tests against the BARs marked as BAR_RESERVED.
    
    After running the BAR tests (which will write to all enabled BARs), the
    inbound address translation is broken. This is because the tegra controller
    exposes the ATU Port Logic Structure in BAR4, so when BAR4 is written, the
    inbound address translation settings get overwritten.
    
    To avoid this, implement the dw_pcie_ep_ops .init() callback and start off
    by disabling all BARs (pci-epf-test will later enable/configure BARs that
    are not defined as BAR_RESERVED).
    
    This matches the behavior of other PCIe endpoint drivers: dra7xx, imx6,
    layerscape-ep, artpec6, dw-rockchip, qcom-ep, rcar-gen4, and uniphier-ep.
    
    With this, the PCI endpoint kselftest test case CONSECUTIVE_BAR_TEST (which
    was specifically made to detect address translation issues) passes.
    
    Fixes: c57247f940e8 ("PCI: tegra: Add support for PCIe endpoint mode in Tegra194")
    Signed-off-by: Niklas Cassel <cassel@kernel.org>
    Signed-off-by: Manivannan Sadhasivam <mani@kernel.org>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250922140822.519796-7-cassel@kernel.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a179d69d45cc6758fa2bb033f9855c1fd18785ff
Author: Vidya Sagar <vidyas@nvidia.com>
Date:   Mon Sep 22 16:08:26 2025 +0200

    PCI: tegra194: Handle errors in BPMP response
    
    commit f8c9ad46b00453a8c075453f3745f8d263f44834 upstream.
    
    The return value from tegra_bpmp_transfer() indicates the success or
    failure of the IPC transaction with BPMP. If the transaction succeeded, we
    also need to check the actual command's result code.
    
    If we don't have error handling for tegra_bpmp_transfer(), we will set the
    pcie->ep_state to EP_STATE_ENABLED even when the tegra_bpmp_transfer()
    command fails. Thus, the pcie->ep_state will get out of sync with reality,
    and any further PERST# assert + deassert will be a no-op and will not
    trigger the hardware initialization sequence.
    
    This is because pex_ep_event_pex_rst_deassert() checks the current
    pcie->ep_state, and does nothing if the current state is already
    EP_STATE_ENABLED.
    
    Thus, it is important to have error handling for tegra_bpmp_transfer(),
    such that the pcie->ep_state can not get out of sync with reality, so that
    we will try to initialize the hardware not only during the first PERST#
    assert + deassert, but also during any succeeding PERST# assert + deassert.
    
    One example where this fix is needed is when using a rock5b as host.
    During the initial PERST# assert + deassert (triggered by the bootloader on
    the rock5b) pex_ep_event_pex_rst_deassert() will get called, but for some
    unknown reason, the tegra_bpmp_transfer() call to initialize the PHY fails.
    Once Linux has been loaded on the rock5b, the PCIe driver will once again
    assert + deassert PERST#. However, without tegra_bpmp_transfer() error
    handling, this second PERST# assert + deassert will not trigger the
    hardware initialization sequence.
    
    With tegra_bpmp_transfer() error handling, the second PERST# assert +
    deassert will once again trigger the hardware to be initialized and this
    time the tegra_bpmp_transfer() succeeds.
    
    Fixes: c57247f940e8 ("PCI: tegra: Add support for PCIe endpoint mode in Tegra194")
    Signed-off-by: Vidya Sagar <vidyas@nvidia.com>
    [cassel: improve commit log]
    Signed-off-by: Niklas Cassel <cassel@kernel.org>
    Signed-off-by: Manivannan Sadhasivam <mani@kernel.org>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Reviewed-by: Jon Hunter <jonathanh@nvidia.com>
    Acked-by: Thierry Reding <treding@nvidia.com>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250922140822.519796-8-cassel@kernel.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a39517be500f5743d1fc11075ab6e5f562ddf530
Author: Niklas Cassel <cassel@kernel.org>
Date:   Mon Sep 22 16:08:24 2025 +0200

    PCI: tegra194: Fix broken tegra_pcie_ep_raise_msi_irq()
    
    commit b640d42a6ac9ba01abe65ec34f7c73aaf6758ab8 upstream.
    
    The pci_epc_raise_irq() supplies a MSI or MSI-X interrupt number in range
    (1-N), as per the pci_epc_raise_irq() kdoc, where N is 32 for MSI.
    
    But tegra_pcie_ep_raise_msi_irq() incorrectly uses the interrupt number as
    the MSI vector. This causes wrong MSI vector to be triggered, leading to
    the failure of PCI endpoint Kselftest MSI_TEST test case.
    
    To fix this issue, convert the interrupt number to MSI vector.
    
    Fixes: c57247f940e8 ("PCI: tegra: Add support for PCIe endpoint mode in Tegra194")
    Signed-off-by: Niklas Cassel <cassel@kernel.org>
    Signed-off-by: Manivannan Sadhasivam <mani@kernel.org>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250922140822.519796-6-cassel@kernel.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit ac83f2b311d22753e162b3663abd300b67a400ff
Author: Marek Vasut <marek.vasut+renesas@mailbox.org>
Date:   Tue Sep 9 18:26:25 2025 +0200

    PCI: rcar-host: Convert struct rcar_msi mask_lock into raw spinlock
    
    commit 5ed35b4d490d8735021cce9b715b62a418310864 upstream.
    
    The rcar_msi_irq_unmask() function may be called from a PCI driver
    request_threaded_irq() function. This triggers kernel/irq/manage.c
    __setup_irq() which locks raw spinlock &desc->lock descriptor lock
    and with that descriptor lock held, calls rcar_msi_irq_unmask().
    
    Since the &desc->lock descriptor lock is a raw spinlock, and the rcar_msi
    .mask_lock is not a raw spinlock, this setup triggers 'BUG: Invalid wait
    context' with CONFIG_PROVE_RAW_LOCK_NESTING=y.
    
    Use scoped_guard() to simplify the locking.
    
    Fixes: 83ed8d4fa656 ("PCI: rcar: Convert to MSI domains")
    Reported-by: Duy Nguyen <duy.nguyen.rh@renesas.com>
    Reported-by: Thuan Nguyen <thuan.nguyen-hong@banvien.com.vn>
    Signed-off-by: Marek Vasut <marek.vasut+renesas@mailbox.org>
    Signed-off-by: Manivannan Sadhasivam <mani@kernel.org>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Reviewed-by: Geert Uytterhoeven <geert+renesas@glider.be>
    Acked-by: Marc Zyngier <maz@kernel.org>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250909162707.13927-2-marek.vasut+renesas@mailbox.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 7a323854c17f91a13e57f7d26a09d72c662cc8a7
Author: Marek Vasut <marek.vasut+renesas@mailbox.org>
Date:   Tue Sep 9 18:26:24 2025 +0200

    PCI: rcar-host: Drop PMSR spinlock
    
    commit 0a8f173d9dad13930d5888505dc4c4fd6a1d4262 upstream.
    
    The pmsr_lock spinlock used to be necessary to synchronize access to the
    PMSR register, because that access could have been triggered from either
    config space access in rcar_pcie_config_access() or an exception handler
    rcar_pcie_aarch32_abort_handler().
    
    The rcar_pcie_aarch32_abort_handler() case is no longer applicable since
    commit 6e36203bc14c ("PCI: rcar: Use PCI_SET_ERROR_RESPONSE after read
    which triggered an exception"), which performs more accurate, controlled
    invocation of the exception, and a fixup.
    
    This leaves rcar_pcie_config_access() as the only call site from which
    rcar_pcie_wakeup() is called. The rcar_pcie_config_access() can only be
    called from the controller struct pci_ops .read and .write callbacks,
    and those are serialized in drivers/pci/access.c using raw spinlock
    'pci_lock' . It should be noted that CONFIG_PCI_LOCKLESS_CONFIG is never
    set on this platform.
    
    Since the 'pci_lock' is a raw spinlock , and the 'pmsr_lock' is not a
    raw spinlock, this constellation triggers 'BUG: Invalid wait context'
    with CONFIG_PROVE_RAW_LOCK_NESTING=y .
    
    Remove the pmsr_lock to fix the locking.
    
    Fixes: a115b1bd3af0 ("PCI: rcar: Add L1 link state fix into data abort hook")
    Reported-by: Duy Nguyen <duy.nguyen.rh@renesas.com>
    Reported-by: Thuan Nguyen <thuan.nguyen-hong@banvien.com.vn>
    Signed-off-by: Marek Vasut <marek.vasut+renesas@mailbox.org>
    Signed-off-by: Manivannan Sadhasivam <mani@kernel.org>
    Reviewed-by: Geert Uytterhoeven <geert+renesas@glider.be>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250909162707.13927-1-marek.vasut+renesas@mailbox.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit fbebd3f8513d8fc6027cc41b90f36c37c2e4132f
Author: Marek Vasut <marek.vasut+renesas@mailbox.org>
Date:   Wed Aug 6 21:25:18 2025 +0200

    PCI: rcar-gen4: Fix PHY initialization
    
    commit d96ac5bdc52b271b4f8ac0670a203913666b8758 upstream.
    
    R-Car V4H Reference Manual R19UH0186EJ0130 Rev.1.30 Apr. 21, 2025 page 4581
    Figure 104.3b Initial Setting of PCIEC(example), middle of the figure
    indicates that fourth write into register 0x148 [2:0] is 0x3 or
    GENMASK(1, 0). The current code writes GENMASK(11, 0) which is a typo. Fix
    the typo.
    
    Fixes: faf5a975ee3b ("PCI: rcar-gen4: Add support for R-Car V4H")
    Signed-off-by: Marek Vasut <marek.vasut+renesas@mailbox.org>
    Signed-off-by: Manivannan Sadhasivam <mani@kernel.org>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250806192548.133140-1-marek.vasut+renesas@mailbox.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 796ed08a0c72076f02b39ce38d76273e6c66b01a
Author: Siddharth Vadapalli <s-vadapalli@ti.com>
Date:   Fri Sep 12 15:37:58 2025 +0530

    PCI: keystone: Use devm_request_irq() to free "ks-pcie-error-irq" on exit
    
    commit e51d05f523e43ce5d2bad957943a2b14f68078cd upstream.
    
    Commit under Fixes introduced the IRQ handler for "ks-pcie-error-irq".
    The interrupt is acquired using "request_irq()" but is never freed if
    the driver exits due to an error. Although the section in the driver that
    invokes "request_irq()" has moved around over time, the issue hasn't been
    addressed until now.
    
    Fix this by using "devm_request_irq()" which automatically frees the
    interrupt if the driver exits.
    
    Fixes: 025dd3daeda7 ("PCI: keystone: Add error IRQ handler")
    Reported-by: Jiri Slaby <jirislaby@kernel.org>
    Closes: https://lore.kernel.org/r/3d3a4b52-e343-42f3-9d69-94c259812143@kernel.org
    Signed-off-by: Siddharth Vadapalli <s-vadapalli@ti.com>
    Signed-off-by: Manivannan Sadhasivam <mani@kernel.org>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250912100802.3136121-2-s-vadapalli@ti.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 68a263cffdaf1fa3f76823cede1abc214b86dad1
Author: Siddharth Vadapalli <s-vadapalli@ti.com>
Date:   Mon Sep 8 17:38:27 2025 +0530

    PCI: j721e: Fix programming sequence of "strap" settings
    
    commit f842d3313ba179d4005096357289c7ad09cec575 upstream.
    
    The Cadence PCIe Controller integrated in the TI K3 SoCs supports both
    Root-Complex and Endpoint modes of operation. The Glue Layer allows
    "strapping" the Mode of operation of the Controller, the Link Speed
    and the Link Width. This is enabled by programming the "PCIEn_CTRL"
    register (n corresponds to the PCIe instance) within the CTRL_MMR
    memory-mapped register space. The "reset-values" of the registers are
    also different depending on the mode of operation.
    
    Since the PCIe Controller latches onto the "reset-values" immediately
    after being powered on, if the Glue Layer configuration is not done while
    the PCIe Controller is off, it will result in the PCIe Controller latching
    onto the wrong "reset-values". In practice, this will show up as a wrong
    representation of the PCIe Controller's capability structures in the PCIe
    Configuration Space. Some such capabilities which are supported by the PCIe
    Controller in the Root-Complex mode but are incorrectly latched onto as
    being unsupported are:
    - Link Bandwidth Notification
    - Alternate Routing ID (ARI) Forwarding Support
    - Next capability offset within Advanced Error Reporting (AER) capability
    
    Fix this by powering off the PCIe Controller before programming the "strap"
    settings and powering it on after that. The runtime PM APIs namely
    pm_runtime_put_sync() and pm_runtime_get_sync() will decrement and
    increment the usage counter respectively, causing GENPD to power off and
    power on the PCIe Controller.
    
    Fixes: f3e25911a430 ("PCI: j721e: Add TI J721E PCIe driver")
    Signed-off-by: Siddharth Vadapalli <s-vadapalli@ti.com>
    Signed-off-by: Manivannan Sadhasivam <mani@kernel.org>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250908120828.1471776-1-s-vadapalli@ti.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit bb47e14c93dbf5e132f134a8e19c8c665a9c970c
Author: Siddharth Vadapalli <s-vadapalli@ti.com>
Date:   Mon Sep 1 17:33:55 2025 +0530

    PCI: j721e: Fix module autoloading
    
    commit 9a7f144e18dc5f037d85a0f0d99524a574331098 upstream.
    
    Commit a2790bf81f0f ("PCI: j721e: Add support to build as a loadable
    module") added support to build the driver as a loadable module. However,
    it did not add MODULE_DEVICE_TABLE() which is required for autoloading the
    driver based on device table when it is built as a loadable module.
    
    Fix it by adding MODULE_DEVICE_TABLE.
    
    Fixes: a2790bf81f0f ("PCI: j721e: Add support to build as a loadable module")
    Signed-off-by: Siddharth Vadapalli <s-vadapalli@ti.com>
    [mani: reworded description]
    Signed-off-by: Manivannan Sadhasivam <mani@kernel.org>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250901120359.3410774-1-s-vadapalli@ti.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 972928e3ea72f991977dfd8d33a57fd8a8bfe7a9
Author: Ilpo Järvinen <ilpo.jarvinen@linux.intel.com>
Date:   Mon Jun 30 17:26:41 2025 +0300

    PCI: Fix failure detection during resource resize
    
    commit 31af09b3eaf3603870ce9fd5a7b6c8693129c4cf upstream.
    
    Since 96336ec70264 ("PCI: Perform reset_resource() and build fail list in
    sync") the failed list is always built and returned to let the caller
    decide what to do with the failures. The caller may want to retry resource
    fitting and assignment and before that can happen, the resources should be
    restored to their original state (a reset effectively clears the struct
    resource), which requires returning them to the failed list so the original
    state remains stored in the associated struct pci_dev_resource.
    
    Resource resizing is different from the ordinary resource fitting and
    assignment in that it only considers part of the resources. This means
    failures for other resource types are not relevant at all and should be
    ignored. As resize doesn't unassign such unrelated resources, those
    resources ending up in the failed list implies assignment of that
    resource must have failed before resize too. The check in
    pci_reassign_bridge_resources() to decide if the whole assignment is
    successful, however, is based on list emptiness which will cause false
    negatives when the failed list has resources with an unrelated type.
    
    If the failed list is not empty, call pci_required_resource_failed() and
    extend it to be able to filter on specific resource types too (if
    provided).
    
    Calling pci_required_resource_failed() at this point is slightly
    problematic because the resource itself is reset when the failed list
    is constructed in __assign_resources_sorted(). As a result,
    pci_resource_is_optional() does not have access to the original
    resource flags. This could be worked around by restoring and
    re-resetting the resource around the call to pci_resource_is_optional(),
    however, it shouldn't cause issue as resource resizing is meant for
    64-bit prefetchable resources according to Christian König (see the
    Link which unfortunately doesn't point directly to Christian's reply
    because lore didn't store that email at all).
    
    Fixes: 96336ec70264 ("PCI: Perform reset_resource() and build fail list in sync")
    Link: https://lore.kernel.org/all/c5d1b5d8-8669-5572-75a7-0b480f581ac1@linux.intel.com/
    Reported-by: D Scott Phillips <scott@os.amperecomputing.com>
    Closes: https://lore.kernel.org/all/86plf0lgit.fsf@scott-ph-mail.amperecomputing.com/
    Signed-off-by: Ilpo Järvinen <ilpo.jarvinen@linux.intel.com>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Tested-by: D Scott Phillips <scott@os.amperecomputing.com>
    Reviewed-by: D Scott Phillips <scott@os.amperecomputing.com>
    Cc: Christian König <christian.koenig@amd.com>
    Cc: stable@vger.kernel.org      # v6.15+
    Link: https://patch.msgid.link/20250822123359.16305-4-ilpo.jarvinen@linux.intel.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 2f952e4eaddf87ccae362d7bace17f7ddd3bfef9
Author: Ilpo Järvinen <ilpo.jarvinen@linux.intel.com>
Date:   Mon Jun 30 17:26:39 2025 +0300

    PCI: Ensure relaxed tail alignment does not increase min_align
    
    commit 6e460c3d611009a1d1c2c1f61c96578284a14fba upstream.
    
    When using relaxed tail alignment for the bridge window, pbus_size_mem()
    also tries to minimize min_align, which can under certain scenarios end up
    increasing min_align from that found by calculate_mem_align().
    
    Ensure min_align is not increased by the relaxed tail alignment.
    
    Eventually, it would be better to add calculate_relaxed_head_align()
    similar to calculate_mem_align() which finds out what alignment can be used
    for the head without introducing any gaps into the bridge window to give
    flexibility on head address too. But that looks relatively complex so it
    requires much more testing than fixing the immediate problem causing a
    regression.
    
    Fixes: 67f9085596ee ("PCI: Allow relaxed bridge window tail sizing for optional resources")
    Reported-by: Rio Liu <rio@r26.me>
    Closes: https://lore.kernel.org/all/o2bL8MtD_40-lf8GlslTw-AZpUPzm8nmfCnJKvS8RQ3NOzOW1uq1dVCEfRpUjJ2i7G2WjfQhk2IWZ7oGp-7G-jXN4qOdtnyOcjRR0PZWK5I=@r26.me/
    Signed-off-by: Ilpo Järvinen <ilpo.jarvinen@linux.intel.com>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Tested-by: Rio Liu <rio@r26.me>
    Cc: stable@vger.kernel.org      # v6.15+
    Link: https://patch.msgid.link/20250822123359.16305-2-ilpo.jarvinen@linux.intel.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 5ff676fc9ed47ecbe39ac819dddcfc3ed9c34a06
Author: Lukas Wunner <lukas@wunner.de>
Date:   Wed Aug 27 15:41:09 2025 +0200

    PCI/AER: Support errors introduced by PCIe r6.0
    
    commit 6633875250b38b18b8638cf01e695de031c71f02 upstream.
    
    PCIe r6.0 defined five additional errors in the Uncorrectable Error
    Status, Mask and Severity Registers (PCIe r7.0 sec 7.8.4.2ff).
    
    lspci has been supporting them since commit 144b0911cc0b ("ls-ecaps:
    extend decode support for more fields for AER CE and UE status"):
    
      https://git.kernel.org/pub/scm/utils/pciutils/pciutils.git/commit/?id=144b0911cc0b
    
    Amend the AER driver to recognize them as well, instead of logging them as
    "Unknown Error Bit".
    
    Signed-off-by: Lukas Wunner <lukas@wunner.de>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Reviewed-by: Kuppuswamy Sathyanarayanan <sathyanarayanan.kuppuswamy@linux.intel.com>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/21f1875b18d4078c99353378f37dcd6b994f6d4e.1756301211.git.lukas@wunner.de
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit e7314ff3928824139aa1cd9c50f47250731dd511
Author: Niklas Schnelle <schnelle@linux.ibm.com>
Date:   Thu Aug 7 15:55:38 2025 +0200

    PCI/AER: Fix missing uevent on recovery when a reset is requested
    
    commit bbf7d0468d0da71d76cc6ec9bc8a224325d07b6b upstream.
    
    Since commit 7b42d97e99d3 ("PCI/ERR: Always report current recovery
    status for udev") AER uses the result of error_detected() as parameter
    to pci_uevent_ers(). As pci_uevent_ers() however does not handle
    PCI_ERS_RESULT_NEED_RESET this results in a missing uevent for the
    beginning of recovery if drivers request a reset. Fix this by treating
    PCI_ERS_RESULT_NEED_RESET as beginning recovery.
    
    Fixes: 7b42d97e99d3 ("PCI/ERR: Always report current recovery status for udev")
    Signed-off-by: Niklas Schnelle <schnelle@linux.ibm.com>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Reviewed-by: Lukas Wunner <lukas@wunner.de>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250807-add_err_uevents-v5-1-adf85b0620b0@linux.ibm.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 3f4e50d0fb794772f06a8ffefd73e2ca10cfe237
Author: Lukas Wunner <lukas@wunner.de>
Date:   Wed Aug 13 07:11:02 2025 +0200

    PCI/ERR: Fix uevent on failure to recover
    
    commit 1cbc5e25fb70e942a7a735a1f3d6dd391afc9b29 upstream.
    
    Upon failure to recover from a PCIe error through AER, DPC or EDR, a
    uevent is sent to inform user space about disconnection of the bridge
    whose subordinate devices failed to recover.
    
    However the bridge itself is not disconnected.  Instead, a uevent should
    be sent for each of the subordinate devices.
    
    Only if the "bridge" happens to be a Root Complex Event Collector or
    Integrated Endpoint does it make sense to send a uevent for it (because
    there are no subordinate devices).
    
    Right now if there is a mix of subordinate devices with and without
    pci_error_handlers, a BEGIN_RECOVERY event is sent for those with
    pci_error_handlers but no FAILED_RECOVERY event is ever sent for them
    afterwards.  Fix it.
    
    Fixes: 856e1eb9bdd4 ("PCI/AER: Add uevents in AER and EEH error/resume")
    Signed-off-by: Lukas Wunner <lukas@wunner.de>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Cc: stable@vger.kernel.org  # v4.16+
    Link: https://patch.msgid.link/68fc527a380821b5d861dd554d2ce42cb739591c.1755008151.git.lukas@wunner.de
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit ee40e5db052d7c6f406fdb95ad639c894c74674c
Author: Niklas Schnelle <schnelle@linux.ibm.com>
Date:   Tue Aug 26 10:52:08 2025 +0200

    PCI/IOV: Add PCI rescan-remove locking when enabling/disabling SR-IOV
    
    commit 05703271c3cdcc0f2a8cf6ebdc45892b8ca83520 upstream.
    
    Before disabling SR-IOV via config space accesses to the parent PF,
    sriov_disable() first removes the PCI devices representing the VFs.
    
    Since commit 9d16947b7583 ("PCI: Add global pci_lock_rescan_remove()")
    such removal operations are serialized against concurrent remove and
    rescan using the pci_rescan_remove_lock. No such locking was ever added
    in sriov_disable() however. In particular when commit 18f9e9d150fc
    ("PCI/IOV: Factor out sriov_add_vfs()") factored out the PCI device
    removal into sriov_del_vfs() there was still no locking around the
    pci_iov_remove_virtfn() calls.
    
    On s390 the lack of serialization in sriov_disable() may cause double
    remove and list corruption with the below (amended) trace being observed:
    
      PSW:  0704c00180000000 0000000c914e4b38 (klist_put+56)
      GPRS: 000003800313fb48 0000000000000000 0000000100000001 0000000000000001
            00000000f9b520a8 0000000000000000 0000000000002fbd 00000000f4cc9480
            0000000000000001 0000000000000000 0000000000000000 0000000180692828
            00000000818e8000 000003800313fe2c 000003800313fb20 000003800313fad8
      #0 [3800313fb20] device_del at c9158ad5c
      #1 [3800313fb88] pci_remove_bus_device at c915105ba
      #2 [3800313fbd0] pci_iov_remove_virtfn at c9152f198
      #3 [3800313fc28] zpci_iov_remove_virtfn at c90fb67c0
      #4 [3800313fc60] zpci_bus_remove_device at c90fb6104
      #5 [3800313fca0] __zpci_event_availability at c90fb3dca
      #6 [3800313fd08] chsc_process_sei_nt0 at c918fe4a2
      #7 [3800313fd60] crw_collect_info at c91905822
      #8 [3800313fe10] kthread at c90feb390
      #9 [3800313fe68] __ret_from_fork at c90f6aa64
      #10 [3800313fe98] ret_from_fork at c9194f3f2.
    
    This is because in addition to sriov_disable() removing the VFs, the
    platform also generates hot-unplug events for the VFs. This being the
    reverse operation to the hotplug events generated by sriov_enable() and
    handled via pdev->no_vf_scan. And while the event processing takes
    pci_rescan_remove_lock and checks whether the struct pci_dev still exists,
    the lack of synchronization makes this checking racy.
    
    Other races may also be possible of course though given that this lack of
    locking persisted so long observable races seem very rare. Even on s390 the
    list corruption was only observed with certain devices since the platform
    events are only triggered by config accesses after the removal, so as long
    as the removal finished synchronously they would not race. Either way the
    locking is missing so fix this by adding it to the sriov_del_vfs() helper.
    
    Just like PCI rescan-remove, locking is also missing in sriov_add_vfs()
    including for the error case where pci_stop_and_remove_bus_device() is
    called without the PCI rescan-remove lock being held. Even in the non-error
    case, adding new PCI devices and buses should be serialized via the PCI
    rescan-remove lock. Add the necessary locking.
    
    Fixes: 18f9e9d150fc ("PCI/IOV: Factor out sriov_add_vfs()")
    Signed-off-by: Niklas Schnelle <schnelle@linux.ibm.com>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Reviewed-by: Benjamin Block <bblock@linux.ibm.com>
    Reviewed-by: Farhan Ali <alifm@linux.ibm.com>
    Reviewed-by: Julian Ruess <julianr@linux.ibm.com>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250826-pci_fix_sriov_disable-v1-1-2d0bc938f2a3@linux.ibm.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f16ab42cc225d656b0bc0a2ccf87a334f74c2d18
Author: Brian Norris <briannorris@google.com>
Date:   Wed Sep 24 09:57:11 2025 -0700

    PCI/sysfs: Ensure devices are powered for config reads
    
    commit 48991e4935078b05f80616c75d1ee2ea3ae18e58 upstream.
    
    The "max_link_width", "current_link_speed", "current_link_width",
    "secondary_bus_number", and "subordinate_bus_number" sysfs files all access
    config registers, but they don't check the runtime PM state. If the device
    is in D3cold or a parent bridge is suspended, we may see -EINVAL, bogus
    values, or worse, depending on implementation details.
    
    Wrap these access in pci_config_pm_runtime_{get,put}() like most of the
    rest of the similar sysfs attributes.
    
    Notably, "max_link_speed" does not access config registers; it returns a
    cached value since d2bd39c0456b ("PCI: Store all PCIe Supported Link
    Speeds").
    
    Fixes: 56c1af4606f0 ("PCI: Add sysfs max_link_speed/width, current_link_speed/width, etc")
    Signed-off-by: Brian Norris <briannorris@google.com>
    Signed-off-by: Brian Norris <briannorris@chromium.org>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250924095711.v2.1.Ibb5b6ca1e2c059e04ec53140cd98a44f2684c668@changeid
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 3d01eb9f5a0a113acee9e2e3f972f825860ac7b6
Author: Marek Vasut <marek.vasut+renesas@mailbox.org>
Date:   Mon Sep 22 17:07:48 2025 +0200

    PCI: tegra: Convert struct tegra_msi mask_lock into raw spinlock
    
    commit 26fda92d3b56bf44a02bcb4001c5a5548e0ae8ee upstream.
    
    The tegra_msi_irq_unmask() function may be called from a PCI driver
    request_threaded_irq() function. This triggers kernel/irq/manage.c
    __setup_irq() which locks raw spinlock &desc->lock descriptor lock
    and with that descriptor lock held, calls tegra_msi_irq_unmask().
    
    Since the &desc->lock descriptor lock is a raw spinlock, and the tegra_msi
    .mask_lock is not a raw spinlock, this setup triggers 'BUG: Invalid wait
    context' with CONFIG_PROVE_RAW_LOCK_NESTING=y.
    
    Use scoped_guard() to simplify the locking.
    
    Fixes: 2c99e55f7955 ("PCI: tegra: Convert to MSI domains")
    Reported-by: Geert Uytterhoeven <geert+renesas@glider.be>
    Closes: https://patchwork.kernel.org/project/linux-pci/patch/20250909162707.13927-2-marek.vasut+renesas@mailbox.org/#26574451
    Signed-off-by: Marek Vasut <marek.vasut+renesas@mailbox.org>
    Signed-off-by: Manivannan Sadhasivam <mani@kernel.org>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250922150811.88450-1-marek.vasut+renesas@mailbox.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 2da2da1e2d3a50c63cad83446a9d616b86120816
Author: Jani Nurminen <jani.nurminen@windriver.com>
Date:   Fri Sep 12 11:09:48 2025 +0200

    PCI: xilinx-nwl: Fix ECAM programming
    
    commit 98a4f5b7359205ced1b6a626df3963bf7c5e5052 upstream.
    
    When PCIe has been set up by the bootloader, the ecam_size field in the
    E_ECAM_CONTROL register already contains a value.
    
    The driver previously programmed it to 0xc (for 16 busses; 16 MB), but
    bumped to 0x10 (for 256 busses; 256 MB) by the commit 2fccd11518f1 ("PCI:
    xilinx-nwl: Modify ECAM size to enable support for 256 buses").
    
    Regardless of what the bootloader has programmed, the driver ORs in a
    new maximal value without doing a proper RMW sequence. This can lead to
    problems.
    
    For example, if the bootloader programs in 0xc and the driver uses 0x10,
    the ORed result is 0x1c, which is beyond the ecam_max_size limit of 0x10
    (from E_ECAM_CAPABILITIES).
    
    Avoid the problems by doing a proper RMW.
    
    Fixes: 2fccd11518f1 ("PCI: xilinx-nwl: Modify ECAM size to enable support for 256 buses")
    Signed-off-by: Jani Nurminen <jani.nurminen@windriver.com>
    [mani: added stable tag]
    Signed-off-by: Manivannan Sadhasivam <mani@kernel.org>
    Signed-off-by: Bjorn Helgaas <bhelgaas@google.com>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/e83a2af2-af0b-4670-bcf5-ad408571c2b0@windriver.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 9cc2c65b58f6ebef38750ee6df77cba8165cd26d
Author: Sean Christopherson <seanjc@google.com>
Date:   Tue Aug 19 15:29:44 2025 -0700

    rseq/selftests: Use weak symbol reference, not definition, to link with glibc
    
    commit a001cd248ab244633c5fabe4f7c707e13fc1d1cc upstream.
    
    Add "extern" to the glibc-defined weak rseq symbols to convert the rseq
    selftest's usage from weak symbol definitions to weak symbol _references_.
    Effectively re-defining the glibc symbols wreaks havoc when building with
    -fno-common, e.g. generates segfaults when running multi-threaded programs,
    as dynamically linked applications end up with multiple versions of the
    symbols.
    
    Building with -fcommon, which until recently has the been the default for
    GCC and clang, papers over the bug by allowing the linker to resolve the
    weak/tentative definition to glibc's "real" definition.
    
    Note, the symbol itself (or rather its address), not the value of the
    symbol, is set to 0/NULL for unresolved weak symbol references, as the
    symbol doesn't exist and thus can't have a value.  Check for a NULL rseq
    size pointer to handle the scenario where the test is statically linked
    against a libc that doesn't support rseq in any capacity.
    
    Fixes: 3bcbc20942db ("selftests/rseq: Play nice with binaries statically linked against glibc 2.35+")
    Reported-by: Thomas Gleixner <tglx@linutronix.de>
    Suggested-by: Florian Weimer <fweimer@redhat.com>
    Signed-off-by: Sean Christopherson <seanjc@google.com>
    Signed-off-by: Thomas Gleixner <tglx@linutronix.de>
    Reviewed-by: Mathieu Desnoyers <mathieu.desnoyers@efficios.com>
    Cc: stable@vger.kernel.org
    Closes: https://lore.kernel.org/all/87frdoybk4.ffs@tglx
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f40a0c06ef666745e6b417c225a59885e171fbca
Author: Esben Haabendal <esben@geanix.com>
Date:   Fri May 16 09:23:35 2025 +0200

    rtc: interface: Fix long-standing race when setting alarm
    
    commit 795cda8338eab036013314dbc0b04aae728880ab upstream.
    
    As described in the old comment dating back to
    commit 6610e0893b8b ("RTC: Rework RTC code to use timerqueue for events")
    from 2010, we have been living with a race window when setting alarm
    with an expiry in the near future (i.e. next second).
    With 1 second resolution, it can happen that the second ticks after the
    check for the timer having expired, but before the alarm is actually set.
    When this happen, no alarm IRQ is generated, at least not with some RTC
    chips (isl12022 is an example of this).
    
    With UIE RTC timer being implemented on top of alarm irq, being re-armed
    every second, UIE will occasionally fail to work, as an alarm irq lost
    due to this race will stop the re-arming loop.
    
    For now, I have limited the additional expiry check to only be done for
    alarms set to next seconds. I expect it should be good enough, although I
    don't know if we can now for sure that systems with loads could end up
    causing the same problems for alarms set 2 seconds or even longer in the
    future.
    
    I haven't been able to reproduce the problem with this check in place.
    
    Cc: stable@vger.kernel.org
    Signed-off-by: Esben Haabendal <esben@geanix.com>
    Link: https://lore.kernel.org/r/20250516-rtc-uie-irq-fixes-v2-1-3de8e530a39e@geanix.com
    Signed-off-by: Alexandre Belloni <alexandre.belloni@bootlin.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit ce7c3a1ee046216a0f63630f2935307b5e855c30
Author: Esben Haabendal <esben@geanix.com>
Date:   Fri May 16 09:23:39 2025 +0200

    rtc: interface: Ensure alarm irq is enabled when UIE is enabled
    
    commit 9db26d5855d0374d4652487bfb5aacf40821c469 upstream.
    
    When setting a normal alarm, user-space is responsible for using
    RTC_AIE_ON/RTC_AIE_OFF to control if alarm irq should be enabled.
    
    But when RTC_UIE_ON is used, interrupts must be enabled so that the
    requested irq events are generated.
    When RTC_UIE_OFF is used, alarm irq is disabled if there are no other
    alarms queued, so this commit brings symmetry to that.
    
    Signed-off-by: Esben Haabendal <esben@geanix.com>
    Cc: stable@vger.kernel.org
    Link: https://lore.kernel.org/r/20250516-rtc-uie-irq-fixes-v2-5-3de8e530a39e@geanix.com
    Signed-off-by: Alexandre Belloni <alexandre.belloni@bootlin.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit bd1300e3d896a13f20ac6ad8fd47df90a61bd847
Author: Patrice Chotard <patrice.chotard@foss.st.com>
Date:   Thu Aug 7 09:34:09 2025 +0200

    memory: stm32_omm: Fix req2ack update test
    
    commit d140f3ba76ac98faad7f9b37ef5a3dcbd57f59e2 upstream.
    
    If "st,omm-req2ack-ns" property is found and its value is not 0,
    the current test doesn't allow to compute and set req2ack value,
    Fix this test.
    
    Fixes: 8181d061dcff ("memory: Add STM32 Octo Memory Manager driver")
    Signed-off-by: Patrice Chotard <patrice.chotard@foss.st.com>
    Link: https://lore.kernel.org/r/20250807-upstream_omm_fix_req2ack_test_condition-v2-1-d7df4af2b48b@foss.st.com
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Krzysztof Kozlowski <krzysztof.kozlowski@linaro.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a4df83ad83b60f0768c099d84df4d7def7789ece
Author: Zhen Ni <zhen.ni@easystack.cn>
Date:   Wed Aug 6 10:55:38 2025 +0800

    memory: samsung: exynos-srom: Fix of_iomap leak in exynos_srom_probe
    
    commit 6744085079e785dae5f7a2239456135407c58b25 upstream.
    
    The of_platform_populate() call at the end of the function has a
    possible failure path, causing a resource leak.
    
    Replace of_iomap() with devm_platform_ioremap_resource() to ensure
    automatic cleanup of srom->reg_base.
    
    This issue was detected by smatch static analysis:
    drivers/memory/samsung/exynos-srom.c:155 exynos_srom_probe()warn:
    'srom->reg_base' from of_iomap() not released on lines: 155.
    
    Fixes: 8ac2266d8831 ("memory: samsung: exynos-srom: Add support for bank configuration")
    Cc: stable@vger.kernel.org
    Signed-off-by: Zhen Ni <zhen.ni@easystack.cn>
    Link: https://lore.kernel.org/r/20250806025538.306593-1-zhen.ni@easystack.cn
    Signed-off-by: Krzysztof Kozlowski <krzysztof.kozlowski@linaro.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit b322ea311497f8cdd75c6d6e273d67f044f533d9
Author: Rex Chen <rex.chen_1@nxp.com>
Date:   Mon Jul 28 17:22:30 2025 +0900

    mmc: mmc_spi: multiple block read remove read crc ack
    
    commit fef12d9f5bcf7e2b19a7cf1295c6abd5642dd241 upstream.
    
    For multiple block read, the current implementation, transfer packet
    includes cmd53 + cmd53 response + block nums*(1byte token +
    block length bytes payload + 2bytes CRC + 1byte transfer), the last
    1byte transfer of every block is not needed, so remove it.
    
    Why doesn't multiple block read need CRC ack?
    For read operation, host side get the payload and CRC value, then
    will only check the CRC value to confirm if the data is correct or
    not, but not send CRC ack to card. If the data is correct, save it,
    or discard it and retransmit if data is error, so the last 1byte
    transfer of every block make no sense.
    
    What's the side effect of this 1byte transfer?
    As the SPI is full duplex, if add this redundant 1byte transfer, SDIO
    card side take it as the token of next block, then all the next sub
    blocks sequence distort.
    
    Signed-off-by: Rex Chen <rex.chen_1@nxp.com>
    Cc: stable@vger.kernel.org
    Link: https://lore.kernel.org/r/20250728082230.1037917-3-rex.chen_1@nxp.com
    Signed-off-by: Ulf Hansson <ulf.hansson@linaro.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit e58bb2cab77ba2cd89576b11e301356f06e491a4
Author: Rex Chen <rex.chen_1@nxp.com>
Date:   Mon Jul 28 17:22:29 2025 +0900

    mmc: core: SPI mode remove cmd7
    
    commit fec40f44afdabcbc4a7748e4278f30737b54bb1a upstream.
    
    SPI mode doesn't support cmd7, so remove it in mmc_sdio_alive() and
    confirm if sdio is active by checking CCCR register value is available
    or not.
    
    Signed-off-by: Rex Chen <rex.chen_1@nxp.com>
    Cc: stable@vger.kernel.org
    Link: https://lore.kernel.org/r/20250728082230.1037917-2-rex.chen_1@nxp.com
    Signed-off-by: Ulf Hansson <ulf.hansson@linaro.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 1da032da3fa37bd6b13d1e23b876ddbbf5312015
Author: Maarten Zanders <maarten@zanders.be>
Date:   Mon Sep 22 17:39:38 2025 +0200

    mtd: nand: raw: gpmi: fix clocks when CONFIG_PM=N
    
    commit 1001cc1171248ebb21d371fbe086b5d3f11b410b upstream.
    
    Commit f04ced6d545e ("mtd: nand: raw: gpmi: improve power management
    handling") moved all clock handling into PM callbacks. With CONFIG_PM
    disabled, those callbacks are missing, leaving the driver unusable.
    
    Add clock init/teardown for !CONFIG_PM builds to restore basic operation.
    Keeping the driver working without requiring CONFIG_PM is preferred over
    adding a Kconfig dependency.
    
    Fixes: f04ced6d545e ("mtd: nand: raw: gpmi: improve power management handling")
    Signed-off-by: Maarten Zanders <maarten@zanders.be>
    Cc: stable@vger.kernel.org
    Signed-off-by: Miquel Raynal <miquel.raynal@bootlin.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 1fa0743b619dfaefda84823bf68e191d58ee8eab
Author: Linus Walleij <linus.walleij@linaro.org>
Date:   Tue Sep 16 18:07:37 2025 +0200

    mtd: rawnand: fsmc: Default to autodetect buswidth
    
    commit b8df622cf7f6808c85764e681847150ed6d85f3d upstream.
    
    If you don't specify buswidth 2 (16 bits) in the device
    tree, FSMC doesn't even probe anymore:
    
    fsmc-nand 10100000.flash: FSMC device partno 090,
      manufacturer 80, revision 00, config 00
    nand: device found, Manufacturer ID: 0x20, Chip ID: 0xb1
    nand: ST Micro 10100000.flash
    nand: bus width 8 instead of 16 bits
    nand: No NAND device found
    fsmc-nand 10100000.flash: probe with driver fsmc-nand failed
      with error -22
    
    With this patch to use autodetection unless buswidth is
    specified, the device is properly detected again:
    
    fsmc-nand 10100000.flash: FSMC device partno 090,
      manufacturer 80, revision 00, config 00
    nand: device found, Manufacturer ID: 0x20, Chip ID: 0xb1
    nand: ST Micro NAND 128MiB 1,8V 16-bit
    nand: 128 MiB, SLC, erase size: 128 KiB, page size: 2048, OOB size: 64
    fsmc-nand 10100000.flash: Using 1-bit HW ECC scheme
    Scanning device for bad blocks
    
    I don't know where or how this happened, I think some change
    in the nand core.
    
    Cc: stable@vger.kernel.org
    Signed-off-by: Linus Walleij <linus.walleij@linaro.org>
    Signed-off-by: Miquel Raynal <miquel.raynal@bootlin.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 5b5fffa7c81e55d8c8edf05ad40d811ec7047e21
Author: Alexander Lobakin <aleksander.lobakin@intel.com>
Date:   Wed Oct 8 18:56:59 2025 +0200

    xsk: Harden userspace-supplied xdp_desc validation
    
    commit 07ca98f906a403637fc5e513a872a50ef1247f3b upstream.
    
    Turned out certain clearly invalid values passed in xdp_desc from
    userspace can pass xp_{,un}aligned_validate_desc() and then lead
    to UBs or just invalid frames to be queued for xmit.
    
    desc->len close to ``U32_MAX`` with a non-zero pool->tx_metadata_len
    can cause positive integer overflow and wraparound, the same way low
    enough desc->addr with a non-zero pool->tx_metadata_len can cause
    negative integer overflow. Both scenarios can then pass the
    validation successfully.
    This doesn't happen with valid XSk applications, but can be used
    to perform attacks.
    
    Always promote desc->len to ``u64`` first to exclude positive
    overflows of it. Use explicit check_{add,sub}_overflow() when
    validating desc->addr (which is ``u64`` already).
    
    bloat-o-meter reports a little growth of the code size:
    
    add/remove: 0/0 grow/shrink: 2/1 up/down: 60/-16 (44)
    Function                                     old     new   delta
    xskq_cons_peek_desc                          299     330     +31
    xsk_tx_peek_release_desc_batch               973    1002     +29
    xsk_generic_xmit                            3148    3132     -16
    
    but hopefully this doesn't hurt the performance much.
    
    Fixes: 341ac980eab9 ("xsk: Support tx_metadata_len")
    Cc: stable@vger.kernel.org # 6.8+
    Signed-off-by: Alexander Lobakin <aleksander.lobakin@intel.com>
    Reviewed-by: Jason Xing <kerneljasonxing@gmail.com>
    Reviewed-by: Maciej Fijalkowski <maciej.fijalkowski@intel.com>
    Link: https://lore.kernel.org/r/20251008165659.4141318-1-aleksander.lobakin@intel.com
    Signed-off-by: Alexei Starovoitov <ast@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a0c2c36d864ef3676b05cfd8c58b72ee3214cb1a
Author: Miaoqian Lin <linmq006@gmail.com>
Date:   Fri Aug 29 16:30:15 2025 +0800

    xtensa: simdisk: add input size check in proc_write_simdisk
    
    commit 5d5f08fd0cd970184376bee07d59f635c8403f63 upstream.
    
    A malicious user could pass an arbitrarily bad value
    to memdup_user_nul(), potentially causing kernel crash.
    
    This follows the same pattern as commit ee76746387f6
    ("netdevsim: prevent bad user input in nsim_dev_health_break_write()")
    
    Fixes: b6c7e873daf7 ("xtensa: ISS: add host file-based simulated disk")
    Fixes: 16e5c1fc3604 ("convert a bunch of open-coded instances of memdup_user_nul()")
    Cc: stable@vger.kernel.org
    Signed-off-by: Miaoqian Lin <linmq006@gmail.com>
    Message-Id: <20250829083015.1992751-1-linmq006@gmail.com>
    Signed-off-by: Max Filippov <jcmvbkbc@gmail.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit c2640cbea354c1f2bff5c67a12676a2cc5712391
Author: Ma Ke <make24@iscas.ac.cn>
Date:   Sat Sep 20 20:53:12 2025 +0800

    sparc: fix error handling in scan_one_device()
    
    commit 302c04110f0ce70d25add2496b521132548cd408 upstream.
    
    Once of_device_register() failed, we should call put_device() to
    decrement reference count for cleanup. Or it could cause memory leak.
    So fix this by calling put_device(), then the name can be freed in
    kobject_cleanup().
    
    Calling path: of_device_register() -> of_device_add() -> device_add().
    As comment of device_add() says, 'if device_add() succeeds, you should
    call device_del() when you want to get rid of it. If device_add() has
    not succeeded, use only put_device() to drop the reference count'.
    
    Found by code review.
    
    Cc: stable@vger.kernel.org
    Fixes: cf44bbc26cf1 ("[SPARC]: Beginnings of generic of_device framework.")
    Signed-off-by: Ma Ke <make24@iscas.ac.cn>
    Reviewed-by: Andreas Larsson <andreas@gaisler.com>
    Signed-off-by: Andreas Larsson <andreas@gaisler.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 5ab2153c2bdf42c1d2305615bacefb35802549d5
Author: Anthony Yznaga <anthony.yznaga@oracle.com>
Date:   Tue Jul 15 18:24:46 2025 -0700

    sparc64: fix hugetlb for sun4u
    
    commit 6fd44a481b3c6111e4801cec964627791d0f3ec5 upstream.
    
    An attempt to exercise sparc hugetlb code in a sun4u-based guest
    running under qemu results in the guest hanging due to being stuck
    in a trap loop. This is due to invalid hugetlb TTEs being installed
    that do not have the expected _PAGE_PMD_HUGE and page size bits set.
    Although the breakage has gone apparently unnoticed for several years,
    fix it now so there is the option to exercise sparc hugetlb code under
    qemu. This can be useful because sun4v support in qemu does not support
    linux guests currently and sun4v-based hardware resources may not be
    readily available.
    
    Fix tested with a 6.15.2 and 6.16-rc6 kernels by running libhugetlbfs
    tests on a qemu guest running Debian 13.
    
    Fixes: c7d9f77d33a7 ("sparc64: Multi-page size support")
    Cc: stable@vger.kernel.org
    Signed-off-by: Anthony Yznaga <anthony.yznaga@oracle.com>
    Tested-by: John Paul Adrian Glaubitz <glaubitz@physik.fu-berlin.de>
    Reviewed-by: John Paul Adrian Glaubitz <glaubitz@physik.fu-berlin.de>
    Reviewed-by: Andreas Larsson <andreas@gaisler.com>
    Link: https://lore.kernel.org/r/20250716012446.10357-1-anthony.yznaga@oracle.com
    Signed-off-by: Andreas Larsson <andreas@gaisler.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 9a527baf53552018908ca55b1df85d757f53b6ae
Author: Bharath SM <bharathsm@microsoft.com>
Date:   Fri Sep 26 10:13:50 2025 -0500

    smb client: fix bug with newly created file in cached dir
    
    commit aa12118dbcfe659697567c9daa0eac2c71e3fd37 upstream.
    
    Test generic/637 spotted a problem with create of a new file in a
    cached directory (by the same client) could cause cases where the
    new file does not show up properly in ls on that client until the
    lease times out.
    
    Fixes: 037e1bae588e ("smb: client: use ParentLeaseKey in cifs_do_create")
    Cc: stable@vger.kernel.org
    Signed-off-by: Bharath SM <bharathsm@microsoft.com>
    Signed-off-by: Steve French <stfrench@microsoft.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 0b32ff285ff6f6f1ac1d9495787ccce8837d6405
Author: Eric Biggers <ebiggers@kernel.org>
Date:   Mon Aug 18 13:54:23 2025 -0700

    sctp: Fix MAC comparison to be constant-time
    
    commit dd91c79e4f58fbe2898dac84858033700e0e99fb upstream.
    
    To prevent timing attacks, MACs need to be compared in constant time.
    Use the appropriate helper function for this.
    
    Fixes: bbd0d59809f9 ("[SCTP]: Implement the receive and verification of AUTH chunk")
    Fixes: 1da177e4c3f4 ("Linux-2.6.12-rc2")
    Cc: stable@vger.kernel.org
    Signed-off-by: Eric Biggers <ebiggers@kernel.org>
    Link: https://patch.msgid.link/20250818205426.30222-3-ebiggers@kernel.org
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 9a75d1c755c3e232d3bb8173a949f392027fa879
Author: Abinash Singh <abinashsinghlalotra@gmail.com>
Date:   Tue Aug 26 00:09:38 2025 +0530

    scsi: sd: Fix build warning in sd_revalidate_disk()
    
    commit b5f717b31b5e478398740db8aee2ecbc4dd72bf3 upstream.
    
    A build warning was triggered due to excessive stack usage in
    sd_revalidate_disk():
    
    drivers/scsi/sd.c: In function ‘sd_revalidate_disk.isra’:
    drivers/scsi/sd.c:3824:1: warning: the frame size of 1160 bytes is larger than 1024 bytes [-Wframe-larger-than=]
    
    This is caused by a large local struct queue_limits (~400B) allocated on
    the stack. Replacing it with a heap allocation using kmalloc()
    significantly reduces frame usage. Kernel stack is limited (~8 KB), and
    allocating large structs on the stack is discouraged.  As the function
    already performs heap allocations (e.g. for buffer), this change fits
    well.
    
    Fixes: 804e498e0496 ("sd: convert to the atomic queue limits API")
    Cc: stable@vger.kernel.org
    Reviewed-by: Bart Van Assche <bvanassche@acm.org>
    Signed-off-by: Abinash Singh <abinashsinghlalotra@gmail.com>
    Link: https://lore.kernel.org/r/20250825183940.13211-2-abinashsinghlalotra@gmail.com
    Reviewed-by: Damien Le Moal <dlemoal@kernel.org>
    Signed-off-by: Martin K. Petersen <martin.petersen@oracle.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 5c9f85f33399046cea0820da9c24fb9277aa979e
Author: Thorsten Blum <thorsten.blum@linux.dev>
Date:   Fri Sep 19 11:26:37 2025 +0200

    scsi: hpsa: Fix potential memory leak in hpsa_big_passthru_ioctl()
    
    commit b81296591c567b12d3873b05a37b975707959b94 upstream.
    
    Replace kmalloc() followed by copy_from_user() with memdup_user() to fix
    a memory leak that occurs when copy_from_user(buff[sg_used],,) fails and
    the 'cleanup1:' path does not free the memory for 'buff[sg_used]'. Using
    memdup_user() avoids this by freeing the memory internally.
    
    Since memdup_user() already allocates memory, use kzalloc() in the else
    branch instead of manually zeroing 'buff[sg_used]' using memset(0).
    
    Cc: stable@vger.kernel.org
    Fixes: edd163687ea5 ("[SCSI] hpsa: add driver for HP Smart Array controllers.")
    Signed-off-by: Thorsten Blum <thorsten.blum@linux.dev>
    Acked-by: Don Brace <don.brace@microchip.com>
    Signed-off-by: Martin K. Petersen <martin.petersen@oracle.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit c8e5a86acfd3007594febffb1876baf173c127ad
Author: Harshit Agarwal <harshit@nutanix.com>
Date:   Tue Apr 8 04:50:21 2025 +0000

    sched/deadline: Fix race in push_dl_task()
    
    commit 8fd5485fb4f3d9da3977fd783fcb8e5452463420 upstream.
    
    When a CPU chooses to call push_dl_task and picks a task to push to
    another CPU's runqueue then it will call find_lock_later_rq method
    which would take a double lock on both CPUs' runqueues. If one of the
    locks aren't readily available, it may lead to dropping the current
    runqueue lock and reacquiring both the locks at once. During this window
    it is possible that the task is already migrated and is running on some
    other CPU. These cases are already handled. However, if the task is
    migrated and has already been executed and another CPU is now trying to
    wake it up (ttwu) such that it is queued again on the runqeue
    (on_rq is 1) and also if the task was run by the same CPU, then the
    current checks will pass even though the task was migrated out and is no
    longer in the pushable tasks list.
    Please go through the original rt change for more details on the issue.
    
    To fix this, after the lock is obtained inside the find_lock_later_rq,
    it ensures that the task is still at the head of pushable tasks list.
    Also removed some checks that are no longer needed with the addition of
    this new check.
    However, the new check of pushable tasks list only applies when
    find_lock_later_rq is called by push_dl_task. For the other caller i.e.
    dl_task_offline_migration, existing checks are used.
    
    Signed-off-by: Harshit Agarwal <harshit@nutanix.com>
    Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
    Acked-by: Juri Lelli <juri.lelli@redhat.com>
    Cc: stable@vger.kernel.org
    Link: https://lore.kernel.org/r/20250408045021.3283624-1-harshit@nutanix.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 8cf5c24533b8058910fcb83a25a9cf0306383780
Author: Corey Minyard <corey@minyard.net>
Date:   Wed Aug 20 11:03:13 2025 -0500

    Revert "ipmi: fix msg stack when IPMI is disconnected"
    
    commit 5d09ee1bec870263f4ace439402ea840503b503b upstream.
    
    This reverts commit c608966f3f9c2dca596967501d00753282b395fc.
    
    This patch has a subtle bug that can cause the IPMI driver to go into an
    infinite loop if the BMC misbehaves in a certain way.  Apparently
    certain BMCs do misbehave this way because several reports have come in
    recently about this.
    
    Signed-off-by: Corey Minyard <corey@minyard.net>
    Tested-by: Eric Hagberg <ehagberg@janestreet.com>
    Cc: <stable@vger.kernel.org> # 6.2
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 14ca48623eec266c73e227314f69bc32cb3a748e
Author: Colin Ian King <colin.i.king@gmail.com>
Date:   Tue Sep 2 14:03:48 2025 +0100

    pwm: Fix incorrect variable used in error message
    
    commit afe872274edc7da46719a2029bfa4eab142b15f6 upstream.
    
    The dev_err message is reporting the incorrect return value ret_tohw,
    it should be reporting the value in ret_fromhw. Fix this by using
    ret_fromhw instead of ret_tohw.
    
    Fixes: 6c5126c6406d ("pwm: Provide new consumer API functions for waveforms")
    Signed-off-by: Colin Ian King <colin.i.king@gmail.com>
    Link: https://lore.kernel.org/r/20250902130348.2630053-1-colin.i.king@gmail.com
    Cc: stable@vger.kernel.org
    Signed-off-by: Uwe Kleine-König <ukleinek@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 6cef9e4425143b19742044c8a675335821fa1994
Author: Jisheng Zhang <jszhang@kernel.org>
Date:   Tue Aug 19 19:42:24 2025 +0800

    pwm: berlin: Fix wrong register in suspend/resume
    
    commit 3a4b9d027e4061766f618292df91760ea64a1fcc upstream.
    
    The 'enable' register should be BERLIN_PWM_EN rather than
    BERLIN_PWM_ENABLE, otherwise, the driver accesses wrong address, there
    will be cpu exception then kernel panic during suspend/resume.
    
    Fixes: bbf0722c1c66 ("pwm: berlin: Add suspend/resume support")
    Signed-off-by: Jisheng Zhang <jszhang@kernel.org>
    Link: https://lore.kernel.org/r/20250819114224.31825-1-jszhang@kernel.org
    Cc: stable@vger.kernel.org
    Signed-off-by: Uwe Kleine-König <ukleinek@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 9932355f56da63c9755e65736cb90871e3f61de8
Author: Nam Cao <namcao@linutronix.de>
Date:   Mon Aug 4 12:07:27 2025 +0200

    powerpc/pseries/msi: Fix potential underflow and leak issue
    
    commit 3443ff3be6e59b80d74036bb39f5b6409eb23cc9 upstream.
    
    pseries_irq_domain_alloc() allocates interrupts at parent's interrupt
    domain. If it fails in the progress, all allocated interrupts are
    freed.
    
    The number of successfully allocated interrupts so far is stored
    "i". However, "i - 1" interrupts are freed. This is broken:
    
      - One interrupt is not be freed
    
      - If "i" is zero, "i - 1" wraps around
    
    Correct the number of freed interrupts to 'i'.
    
    Fixes: a5f3d2c17b07 ("powerpc/pseries/pci: Add MSI domains")
    Signed-off-by: Nam Cao <namcao@linutronix.de>
    Cc: stable@vger.kernel.org
    Reviewed-by: Cédric Le Goater <clg@redhat.com>
    Signed-off-by: Madhavan Srinivasan <maddy@linux.ibm.com>
    Link: https://patch.msgid.link/a980067f2b256bf716b4cd713bc1095966eed8cd.1754300646.git.namcao@linutronix.de
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f13e811ca7f6d3f616a33b81b2fc9c60385b1159
Author: Nam Cao <namcao@linutronix.de>
Date:   Mon Aug 4 12:07:28 2025 +0200

    powerpc/powernv/pci: Fix underflow and leak issue
    
    commit a39087905af9ffecaa237a918a2c03a04e479934 upstream.
    
    pnv_irq_domain_alloc() allocates interrupts at parent's interrupt
    domain. If it fails in the progress, all allocated interrupts are
    freed.
    
    The number of successfully allocated interrupts so far is stored
    "i". However, "i - 1" interrupts are freed. This is broken:
    
        - One interrupt is not be freed
    
        - If "i" is zero, "i - 1" wraps around
    
    Correct the number of freed interrupts to "i".
    
    Fixes: 0fcfe2247e75 ("powerpc/powernv/pci: Add MSI domains")
    Signed-off-by: Nam Cao <namcao@linutronix.de>
    Cc: stable@vger.kernel.org
    Reviewed-by: Cédric Le Goater <clg@redhat.com>
    Signed-off-by: Madhavan Srinivasan <maddy@linux.ibm.com>
    Link: https://patch.msgid.link/70f8debe8688e0b467367db769b71c20146a836d.1754300646.git.namcao@linutronix.de
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 36067f5ab90964cdf56cd778902b649df1c38b3d
Author: Dzmitry Sankouski <dsankouski@gmail.com>
Date:   Thu Sep 18 20:06:45 2025 +0300

    power: supply: max77976_charger: fix constant current reporting
    
    commit ee6cd8f3e28ee5a929c3b67c01a350f550f9b73a upstream.
    
    CHARGE_CONTROL_LIMIT is a wrong property to report charge current limit,
    because `CHARGE_*` attributes represents capacity, not current. The
    correct attribute to report and set charge current limit is
    CONSTANT_CHARGE_CURRENT.
    
    Rename CHARGE_CONTROL_LIMIT to CONSTANT_CHARGE_CURRENT.
    
    Cc: stable@vger.kernel.org
    Fixes: 715ecbc10d6a ("power: supply: max77976: add Maxim MAX77976 charger driver")
    Signed-off-by: Dzmitry Sankouski <dsankouski@gmail.com>
    Signed-off-by: Sebastian Reichel <sebastian.reichel@collabora.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 17b6b781719db1caebf40ed239173dc55ce69f46
Author: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Date:   Fri Sep 26 18:40:25 2025 +0200

    PM: hibernate: Restrict GFP mask in power_down()
    
    commit 6f4c6f9ed4ce65303f6bb153e2afc71bc33c8ded upstream.
    
    Commit 12ffc3b1513e ("PM: Restrict swap use to later in the
    suspend sequence") caused hibernation_platform_enter() to call
    pm_restore_gfp_mask() via dpm_resume_end(), so when power_down()
    returns after aborting hibernation_platform_enter(), it needs
    to match the pm_restore_gfp_mask() call in hibernate() that will
    occur subsequently.
    
    Address this by adding a pm_restrict_gfp_mask() call to the relevant
    error path in power_down().
    
    Fixes: 12ffc3b1513e ("PM: Restrict swap use to later in the suspend sequence")
    Cc: 6.16+ <stable@vger.kernel.org> # 6.16+
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Reviewed-by: Mario Limonciello (AMD) <superm1@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 7425ca69f328b2ae06403d376c202296a6b7e2da
Author: Mario Limonciello (AMD) <superm1@kernel.org>
Date:   Thu Sep 25 13:51:06 2025 -0500

    PM: hibernate: Fix hybrid-sleep
    
    commit 469d80a3712c66a00b5bb888e62e809db8887ba7 upstream.
    
    Hybrid sleep will hibernate the system followed by running through
    the suspend routine.  Since both the hibernate and the suspend routine
    will call pm_restrict_gfp_mask(), pm_restore_gfp_mask() must be called
    before starting the suspend sequence.
    
    Add an explicit call to pm_restore_gfp_mask() to power_down() before
    the suspend sequence starts. Add an extra call for pm_restrict_gfp_mask()
    when exiting suspend so that the pm_restore_gfp_mask() call in hibernate()
    is balanced.
    
    Reported-by: Ionut Nechita <ionut_n2001@yahoo.com>
    Closes: https://gitlab.freedesktop.org/drm/amd/-/issues/4573
    Tested-by: Ionut Nechita <ionut_n2001@yahoo.com>
    Fixes: 12ffc3b1513eb ("PM: Restrict swap use to later in the suspend sequence")
    Tested-by: Kenneth Crudup <kenny@panix.com>
    Acked-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Mario Limonciello (AMD) <superm1@kernel.org>
    Link: https://patch.msgid.link/20250925185108.2968494-2-superm1@kernel.org
    [ rjw: Add comment explainig the new pm_restrict_gfp_mask() call purpose ]
    Cc: 6.16+ <stable@vger.kernel.org> # 6.16+
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit cdbebde87573145112ce69241f6877023349c692
Author: Christian Loehle <christian.loehle@arm.com>
Date:   Sun Aug 31 22:43:57 2025 +0100

    PM: EM: Fix late boot with holes in CPU topology
    
    commit 1ebe8f7e782523e62cd1fa8237f7afba5d1dae83 upstream.
    
    Commit e3f1164fc9ee ("PM: EM: Support late CPUs booting and capacity
    adjustment") added a mechanism to handle CPUs that come up late by
    retrying when any of the `cpufreq_cpu_get()` call fails.
    
    However, if there are holes in the CPU topology (offline CPUs, e.g.
    nosmt), the first missing CPU causes the loop to break, preventing
    subsequent online CPUs from being updated.
    
    Instead of aborting on the first missing CPU policy, loop through all
    and retry if any were missing.
    
    Fixes: e3f1164fc9ee ("PM: EM: Support late CPUs booting and capacity adjustment")
    Suggested-by: Kenneth Crudup <kenneth.crudup@gmail.com>
    Reported-by: Kenneth Crudup <kenneth.crudup@gmail.com>
    Link: https://lore.kernel.org/linux-pm/40212796-734c-4140-8a85-854f72b8144d@panix.com/
    Cc: 6.9+ <stable@vger.kernel.org> # 6.9+
    Signed-off-by: Christian Loehle <christian.loehle@arm.com>
    Link: https://patch.msgid.link/20250831214357.2020076-1-christian.loehle@arm.com
    [ rjw: Drop the new pr_debug() message which is not very useful ]
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 33ca88c5eb12972d808510735d2f2653d3d7d2d4
Author: Krzysztof Kozlowski <krzysztof.kozlowski@linaro.org>
Date:   Sat Aug 30 13:16:58 2025 +0200

    pinctrl: samsung: Drop unused S3C24xx driver data
    
    commit 358253fa8179ab4217ac283b56adde0174186f87 upstream.
    
    Drop unused declarations after S3C24xx SoC family removal in the commit
    61b7f8920b17 ("ARM: s3c: remove all s3c24xx support").
    
    Fixes: 1ea35b355722 ("ARM: s3c: remove s3c24xx specific hacks")
    Cc: stable@vger.kernel.org
    Link: https://lore.kernel.org/r/20250830111657.126190-3-krzysztof.kozlowski@linaro.org
    Signed-off-by: Krzysztof Kozlowski <krzysztof.kozlowski@linaro.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 80a8b2a9b1ce6452ad21722f9cedae24ff44d9ad
Author: Georg Gottleuber <ggo@tuxedocomputers.com>
Date:   Tue Jul 1 22:55:49 2025 +0200

    nvme-pci: Add TUXEDO IBS Gen8 to Samsung sleep quirk
    
    commit eeaed48980a7aeb0d3d8b438185d4b5a66154ff9 upstream.
    
    On the TUXEDO InfinityBook S Gen8, a Samsung 990 Evo NVMe leads to
    a high power consumption in s2idle sleep (3.5 watts).
    
    This patch applies 'Force No Simple Suspend' quirk to achieve a sleep with
    a lower power consumption, typically around 1 watts.
    
    Signed-off-by: Georg Gottleuber <ggo@tuxedocomputers.com>
    Signed-off-by: Werner Sembach <wse@tuxedocomputers.com>
    Cc: stable@vger.kernel.org
    Signed-off-by: Keith Busch <kbusch@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 47f0373c39b27f0854fc0bb098cea62c8c203486
Author: John David Anglin <dave.anglin@bell.net>
Date:   Tue Aug 5 11:35:30 2025 -0400

    parisc: Remove spurious if statement from raw_copy_from_user()
    
    commit 16794e524d310780163fdd49d0bf7fac30f8dbc8 upstream.
    
    Accidently introduced in commit 91428ca9320e.
    
    Signed-off-by: John David Anglin <dave.anglin@bell.net>
    Signed-off-by: Helge Deller <deller@gmx.de>
    Fixes: 91428ca9320e ("parisc: Check region is readable by user in raw_copy_from_user()")
    Cc: stable@vger.kernel.org # v5.12+
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 4210e5e642da2bfed303ee6a7b16a10cea56d4e6
Author: Sam James <sam@gentoo.org>
Date:   Wed Oct 1 23:58:40 2025 +0100

    parisc: don't reference obsolete termio struct for TC* constants
    
    commit 8ec5a066f88f89bd52094ba18792b34c49dcd55a upstream.
    
    Similar in nature to ab107276607af90b13a5994997e19b7b9731e251. glibc-2.42
    drops the legacy termio struct, but the ioctls.h header still defines some
    TC* constants in terms of termio (via sizeof). Hardcode the values instead.
    
    This fixes building Python for example, which falls over like:
      ./Modules/termios.c:1119:16: error: invalid application of 'sizeof' to incomplete type 'struct termio'
    
    Link: https://bugs.gentoo.org/961769
    Link: https://bugs.gentoo.org/962600
    Co-authored-by: Stian Halseth <stian@itx.no>
    Cc: stable@vger.kernel.org
    Signed-off-by: Sam James <sam@gentoo.org>
    Signed-off-by: Helge Deller <deller@gmx.de>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a68c1d41459314428a0f69c774b1bd83c6fce7a6
Author: Xiao Liang <shaw.leon@gmail.com>
Date:   Sun Aug 17 00:30:15 2025 +0800

    padata: Reset next CPU when reorder sequence wraps around
    
    commit 501302d5cee0d8e8ec2c4a5919c37e0df9abc99b upstream.
    
    When seq_nr wraps around, the next reorder job with seq 0 is hashed to
    the first CPU in padata_do_serial(). Correspondingly, need reset pd->cpu
    to the first one when pd->processed wraps around. Otherwise, if the
    number of used CPUs is not a power of 2, padata_find_next() will be
    checking a wrong list, hence deadlock.
    
    Fixes: 6fc4dbcf0276 ("padata: Replace delayed timer with immediate workqueue in padata_reorder")
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Xiao Liang <shaw.leon@gmail.com>
    Signed-off-by: Herbert Xu <herbert@gondor.apana.org.au>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 066c9afe6b5611aa164902cb342d5ffa25a859ac
Author: Askar Safin <safinaskar@zohomail.com>
Date:   Mon Aug 25 18:12:33 2025 +0000

    openat2: don't trigger automounts with RESOLVE_NO_XDEV
    
    commit 042a60680de43175eb4df0977ff04a4eba9da082 upstream.
    
    openat2 had a bug: if we pass RESOLVE_NO_XDEV, then openat2
    doesn't traverse through automounts, but may still trigger them.
    (See the link for full bug report with reproducer.)
    
    This commit fixes this bug.
    
    Link: https://lore.kernel.org/linux-fsdevel/20250817075252.4137628-1-safinaskar@zohomail.com/
    Fixes: fddb5d430ad9fa91b49b1 ("open: introduce openat2(2) syscall")
    Reviewed-by: Aleksa Sarai <cyphar@cyphar.com>
    Cc: stable@vger.kernel.org
    Signed-off-by: Askar Safin <safinaskar@zohomail.com>
    Link: https://lore.kernel.org/20250825181233.2464822-5-safinaskar@zohomail.com
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 65074c41d794edd06858fa366e0f6d65ef5f42aa
Author: Ma Ke <make24@iscas.ac.cn>
Date:   Tue Sep 30 16:16:18 2025 +0800

    of: unittest: Fix device reference count leak in of_unittest_pci_node_verify
    
    commit a8de554774ae48efbe48ace79f8badae2daa2bf1 upstream.
    
    In of_unittest_pci_node_verify(), when the add parameter is false,
    device_find_any_child() obtains a reference to a child device. This
    function implicitly calls get_device() to increment the device's
    reference count before returning the pointer. However, the caller
    fails to properly release this reference by calling put_device(),
    leading to a device reference count leak. Add put_device() in the else
    branch immediately after child_dev is no longer needed.
    
    As the comment of device_find_any_child states: "NOTE: you will need
    to drop the reference with put_device() after use".
    
    Found by code review.
    
    Cc: stable@vger.kernel.org
    Fixes: 26409dd04589 ("of: unittest: Add pci_dt_testdrv pci driver")
    Signed-off-by: Ma Ke <make24@iscas.ac.cn>
    Signed-off-by: Rob Herring (Arm) <robh@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 2cf75878ee59c69c8b3eac96743e85ec67d83ded
Author: Yu Kuai <yukuai3@huawei.com>
Date:   Wed Sep 10 14:30:44 2025 +0800

    md: fix mssing blktrace bio split events
    
    commit 22f166218f7313e8fe2d19213b5f4b3265f8c39e upstream.
    
    If bio is split by internal handling like chunksize or badblocks, the
    corresponding trace_block_split() is missing, resulting in blktrace
    inability to catch BIO split events and making it harder to analyze the
    BIO sequence.
    
    Cc: stable@vger.kernel.org
    Fixes: 4b1faf931650 ("block: Kill bio_pair_split()")
    Signed-off-by: Yu Kuai <yukuai3@huawei.com>
    Reviewed-by: Damien Le Moal <dlemoal@kernel.org>
    Reviewed-by: Christoph Hellwig <hch@lst.de>
    Signed-off-by: Jens Axboe <axboe@kernel.dk>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit da716ce37862c6323df0074115847a9375035919
Author: Li Chen <me@linux.beauty>
Date:   Tue Sep 30 08:35:59 2025 +0800

    loop: fix backing file reference leak on validation error
    
    commit 98b7bf54338b797e3a11e8178ce0e806060d8fa3 upstream.
    
    loop_change_fd() and loop_configure() call loop_check_backing_file()
    to validate the new backing file. If validation fails, the reference
    acquired by fget() was not dropped, leaking a file reference.
    
    Fix this by calling fput(file) before returning the error.
    
    Cc: stable@vger.kernel.org
    Cc: Markus Elfring <Markus.Elfring@web.de>
    CC: Yang Erkun <yangerkun@huawei.com>
    Cc: Ming Lei <ming.lei@redhat.com>
    Cc: Yu Kuai <yukuai1@huaweicloud.com>
    Fixes: f5c84eff634b ("loop: Add sanity check for read/write_iter")
    Signed-off-by: Li Chen <chenl311@chinatelecom.cn>
    Reviewed-by: Ming Lei <ming.lei@redhat.com>
    Reviewed-by: Yang Erkun <yangerkun@huawei.com>
    Signed-off-by: Jens Axboe <axboe@kernel.dk>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 00d9c4a822c44fc64261e2f38e7bb40981fecb08
Author: Johan Hovold <johan@kernel.org>
Date:   Wed Sep 24 10:02:07 2025 +0200

    lib/genalloc: fix device leak in of_gen_pool_get()
    
    commit 1260cbcffa608219fc9188a6cbe9c45a300ef8b5 upstream.
    
    Make sure to drop the reference taken when looking up the genpool platform
    device in of_gen_pool_get() before returning the pool.
    
    Note that holding a reference to a device does typically not prevent its
    devres managed resources from being released so there is no point in
    keeping the reference.
    
    Link: https://lkml.kernel.org/r/20250924080207.18006-1-johan@kernel.org
    Fixes: 9375db07adea ("genalloc: add devres support, allow to find a managed pool by device")
    Signed-off-by: Johan Hovold <johan@kernel.org>
    Cc: Philipp Zabel <p.zabel@pengutronix.de>
    Cc: Vladimir Zapolskiy <vz@mleia.com>
    Cc: <stable@vger.kernel.org>    [3.10+]
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 8f4abe676eaa8079bdf9fc5457a85162d0aa17aa
Author: Pratyush Yadav <pratyush@kernel.org>
Date:   Thu Sep 18 19:06:15 2025 +0200

    kho: only fill kimage if KHO is finalized
    
    commit f322a97aeb2a05b6b1ee17629145eb02e1a4c6a0 upstream.
    
    kho_fill_kimage() only checks for KHO being enabled before filling in the
    FDT to the image.  KHO being enabled does not mean that the kernel has
    data to hand over.  That happens when KHO is finalized.
    
    When a kexec is done with KHO enabled but not finalized, the FDT page is
    allocated but not initialized.  FDT initialization happens after finalize.
    This means the KHO segment is filled in but the FDT contains garbage
    data.
    
    This leads to the below error messages in the next kernel:
    
        [    0.000000] KHO: setup: handover FDT (0x10116b000) is invalid: -9
        [    0.000000] KHO: disabling KHO revival: -22
    
    There is no problem in practice, and the next kernel boots and works fine.
    But this still leads to misleading error messages and garbage being
    handed over.
    
    Only fill in KHO segment when KHO is finalized.  When KHO is not enabled,
    the debugfs interface is not created and there is no way to finalize it
    anyway.  So the check for kho_enable is not needed, and kho_out.finalize
    alone is enough.
    
    Link: https://lkml.kernel.org/r/20250918170617.91413-1-pratyush@kernel.org
    Fixes: 3bdecc3c93f9 ("kexec: add KHO support to kexec file loads")
    Signed-off-by: Pratyush Yadav <pratyush@kernel.org>
    Reviewed-by: Mike Rapoport (Microsoft) <rppt@kernel.org>
    Cc: Alexander Graf <graf@amazon.com>
    Cc: Baoquan He <bhe@redhat.com>
    Cc: Changyuan Lyu <changyuanl@google.com>
    Cc: Jason Gunthorpe <jgg@nvidia.com>
    Cc: Pasha Tatashin <pasha.tatashin@soleen.com>
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 7ac82e0710acd0ef4cedb930d5077c12e9172c1e
Author: Eric Biggers <ebiggers@kernel.org>
Date:   Sat Aug 9 10:19:39 2025 -0700

    KEYS: trusted_tpm1: Compare HMAC values in constant time
    
    commit eed0e3d305530066b4fc5370107cff8ef1a0d229 upstream.
    
    To prevent timing attacks, HMAC value comparison needs to be constant
    time.  Replace the memcmp() with the correct function, crypto_memneq().
    
    [For the Fixes commit I used the commit that introduced the memcmp().
    It predates the introduction of crypto_memneq(), but it was still a bug
    at the time even though a helper function didn't exist yet.]
    
    Fixes: d00a1c72f7f4 ("keys: add new trusted key-type")
    Cc: stable@vger.kernel.org
    Signed-off-by: Eric Biggers <ebiggers@kernel.org>
    Reviewed-by: Jarkko Sakkinen <jarkko@kernel.org>
    Signed-off-by: Jarkko Sakkinen <jarkko@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 6796412decd2d8de8ec708213bbc958fab72f143
Author: Oleg Nesterov <oleg@redhat.com>
Date:   Mon Sep 15 14:09:17 2025 +0200

    kernel/sys.c: fix the racy usage of task_lock(tsk->group_leader) in sys_prlimit64() paths
    
    commit a15f37a40145c986cdf289a4b88390f35efdecc4 upstream.
    
    The usage of task_lock(tsk->group_leader) in sys_prlimit64()->do_prlimit()
    path is very broken.
    
    sys_prlimit64() does get_task_struct(tsk) but this only protects task_struct
    itself. If tsk != current and tsk is not a leader, this process can exit/exec
    and task_lock(tsk->group_leader) may use the already freed task_struct.
    
    Another problem is that sys_prlimit64() can race with mt-exec which changes
    ->group_leader. In this case do_prlimit() may take the wrong lock, or (worse)
    ->group_leader may change between task_lock() and task_unlock().
    
    Change sys_prlimit64() to take tasklist_lock when necessary. This is not
    nice, but I don't see a better fix for -stable.
    
    Link: https://lkml.kernel.org/r/20250915120917.GA27702@redhat.com
    Fixes: 18c91bb2d872 ("prlimit: do not grab the tasklist_lock")
    Signed-off-by: Oleg Nesterov <oleg@redhat.com>
    Cc: Christian Brauner <brauner@kernel.org>
    Cc: Jiri Slaby <jirislaby@kernel.org>
    Cc: Mateusz Guzik <mjguzik@gmail.com>
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit b937637ff4c873036440c2e3581ff03227c6ae41
Author: Corey Minyard <corey@minyard.net>
Date:   Tue Aug 19 13:11:39 2025 -0500

    ipmi:msghandler:Change seq_lock to a mutex
    
    commit 8fd8ea2869cfafb3b1d6f95ff49561b13a73438d upstream.
    
    Dan Carpenter got a Smatch warning:
    
            drivers/char/ipmi/ipmi_msghandler.c:5265 ipmi_free_recv_msg()
            warn: sleeping in atomic context
    
    due to the recent rework of the IPMI driver's locking.  I didn't realize
    vfree could block.  But there is an easy solution to this, now that
    almost everything in the message handler runs in thread context.
    
    I wanted to spend the time earlier to see if seq_lock could be converted
    from a spinlock to a mutex, but I wanted the previous changes to go in
    and soak before I did that.  So I went ahead and did the analysis and
    converting should work.  And solve this problem.
    
    Reported-by: kernel test robot <lkp@intel.com>
    Reported-by: Dan Carpenter <dan.carpenter@linaro.org>
    Closes: https://lore.kernel.org/r/202503240244.LR7pOwyr-lkp@intel.com/
    Fixes: 3be997d5a64a ("ipmi:msghandler: Remove srcu from the ipmi user structure")
    Cc: <stable@vger.kernel.org> # 6.16
    Signed-off-by: Corey Minyard <corey@minyard.net>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 0ed73be9a2547ffb9b5c1d879ad9bfab73d920b5
Author: Corey Minyard <corey@minyard.net>
Date:   Fri Sep 5 11:33:39 2025 -0500

    ipmi: Rework user message limit handling
    
    commit b52da4054ee0bf9ecb44996f2c83236ff50b3812 upstream.
    
    The limit on the number of user messages had a number of issues,
    improper counting in some cases and a use after free.
    
    Restructure how this is all done to handle more in the receive message
    allocation routine, so all refcouting and user message limit counts
    are done in that routine.  It's a lot cleaner and safer.
    
    Reported-by: Gilles BULOZ <gilles.buloz@kontron.com>
    Closes: https://lore.kernel.org/lkml/aLsw6G0GyqfpKs2S@mail.minyard.net/
    Fixes: 8e76741c3d8b ("ipmi: Add a limit on the number of users that may use IPMI")
    Cc: <stable@vger.kernel.org> # 4.19
    Signed-off-by: Corey Minyard <corey@minyard.net>
    Tested-by: Gilles BULOZ <gilles.buloz@kontron.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit dc46e9ca384c1a20237762fb188dccbcc48c586b
Author: Lu Baolu <baolu.lu@linux.intel.com>
Date:   Thu Sep 18 13:02:02 2025 +0800

    iommu/vt-d: PRS isn't usable if PDS isn't supported
    
    commit 5ef7e24c742038a5d8c626fdc0e3a21834358341 upstream.
    
    The specification, Section 7.10, "Software Steps to Drain Page Requests &
    Responses," requires software to submit an Invalidation Wait Descriptor
    (inv_wait_dsc) with the Page-request Drain (PD=1) flag set, along with
    the Invalidation Wait Completion Status Write flag (SW=1). It then waits
    for the Invalidation Wait Descriptor's completion.
    
    However, the PD field in the Invalidation Wait Descriptor is optional, as
    stated in Section 6.5.2.9, "Invalidation Wait Descriptor":
    
    "Page-request Drain (PD): Remapping hardware implementations reporting
     Page-request draining as not supported (PDS = 0 in ECAP_REG) treat this
     field as reserved."
    
    This implies that if the IOMMU doesn't support the PDS capability, software
    can't drain page requests and group responses as expected.
    
    Do not enable PCI/PRI if the IOMMU doesn't support PDS.
    
    Reported-by: Joel Granados <joel.granados@kernel.org>
    Closes: https://lore.kernel.org/r/20250909-jag-pds-v1-1-ad8cba0e494e@kernel.org
    Fixes: 66ac4db36f4c ("iommu/vt-d: Add page request draining support")
    Cc: stable@vger.kernel.org
    Signed-off-by: Lu Baolu <baolu.lu@linux.intel.com>
    Link: https://lore.kernel.org/r/20250915062946.120196-1-baolu.lu@linux.intel.com
    Signed-off-by: Joerg Roedel <joerg.roedel@amd.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 57fe5dae7aa28106e99caf94969f8131f086f31e
Author: Sean Nyekjaer <sean@geanix.com>
Date:   Mon Sep 1 09:49:15 2025 +0200

    iio: imu: inv_icm42600: Avoid configuring if already pm_runtime suspended
    
    commit 466f7a2fef2a4e426f809f79845a1ec1aeb558f4 upstream.
    
    Do as in suspend, skip resume configuration steps if the device is already
    pm_runtime suspended. This avoids reconfiguring a device that is already
    in the correct low-power state and ensures that pm_runtime handles the
    power state transitions properly.
    
    Fixes: 31c24c1e93c3 ("iio: imu: inv_icm42600: add core of new inv_icm42600 driver")
    Signed-off-by: Sean Nyekjaer <sean@geanix.com>
    Link: https://patch.msgid.link/20250901-icm42pmreg-v3-3-ef1336246960@geanix.com
    Cc: <Stable@vger.kernel.org>
    Signed-off-by: Jonathan Cameron <Jonathan.Cameron@huawei.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 4f4b7a5a9db7d2e9eda8cf8dbea53c9afdbafc86
Author: Sean Nyekjaer <sean@geanix.com>
Date:   Mon Sep 1 09:49:14 2025 +0200

    iio: imu: inv_icm42600: Drop redundant pm_runtime reinitialization in resume
    
    commit a95a0b4e471a6d8860f40c6ac8f1cad9dde3189a upstream.
    
    Remove unnecessary calls to pm_runtime_disable(), pm_runtime_set_active(),
    and pm_runtime_enable() from the resume path. These operations are not
    required here and can interfere with proper pm_runtime state handling,
    especially when resuming from a pm_runtime suspended state.
    
    Fixes: 31c24c1e93c3 ("iio: imu: inv_icm42600: add core of new inv_icm42600 driver")
    Signed-off-by: Sean Nyekjaer <sean@geanix.com>
    Link: https://patch.msgid.link/20250901-icm42pmreg-v3-2-ef1336246960@geanix.com
    Cc: <Stable@vger.kernel.org>
    Signed-off-by: Jonathan Cameron <Jonathan.Cameron@huawei.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 4520b708fd744a9966dc6ed0e6d71d7a031eb604
Author: Sean Nyekjaer <sean@geanix.com>
Date:   Mon Sep 1 09:49:13 2025 +0200

    iio: imu: inv_icm42600: Simplify pm_runtime setup
    
    commit 0792c1984a45ccd7a296d6b8cb78088bc99a212e upstream.
    
    Rework the power management in inv_icm42600_core_probe() to use
    devm_pm_runtime_set_active_enabled(), which simplifies the runtime PM
    setup by handling activation and enabling in one step.
    Remove the separate inv_icm42600_disable_pm callback, as it's no longer
    needed with the devm-managed approach.
    Using devm_pm_runtime_enable() also fixes the missing disable of
    autosuspend.
    Update inv_icm42600_disable_vddio_reg() to only disable the regulator if
    the device is not suspended i.e. powered-down, preventing unbalanced
    disables.
    Also remove redundant error msg on regulator_disable(), the regulator
    framework already emits an error message when regulator_disable() fails.
    
    This simplifies the PM setup and avoids manipulating the usage counter
    unnecessarily.
    
    Fixes: 31c24c1e93c3 ("iio: imu: inv_icm42600: add core of new inv_icm42600 driver")
    Signed-off-by: Sean Nyekjaer <sean@geanix.com>
    Link: https://patch.msgid.link/20250901-icm42pmreg-v3-1-ef1336246960@geanix.com
    Cc: <Stable@vger.kernel.org>
    Signed-off-by: Jonathan Cameron <Jonathan.Cameron@huawei.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 41d53bc056ae5fdd7d9124cb6f411ba68c25bda4
Author: Huacai Chen <chenhuacai@kernel.org>
Date:   Mon Jul 21 18:13:43 2025 +0800

    init: handle bootloader identifier in kernel parameters
    
    commit e416f0ed3c500c05c55fb62ee62662717b1c7f71 upstream.
    
    BootLoaders (Grub, LILO, etc) may pass an identifier such as "BOOT_IMAGE=
    /boot/vmlinuz-x.y.z" to kernel parameters.  But these identifiers are not
    recognized by the kernel itself so will be passed to userspace.  However
    user space init program also don't recognize it.
    
    KEXEC/KDUMP (kexec-tools) may also pass an identifier such as "kexec" on
    some architectures.
    
    We cannot change BootLoader's behavior, because this behavior exists for
    many years, and there are already user space programs search BOOT_IMAGE=
    in /proc/cmdline to obtain the kernel image locations:
    
    https://github.com/linuxdeepin/deepin-ab-recovery/blob/master/util.go
    (search getBootOptions)
    https://github.com/linuxdeepin/deepin-ab-recovery/blob/master/main.go
    (search getKernelReleaseWithBootOption) So the the best way is handle
    (ignore) it by the kernel itself, which can avoid such boot warnings (if
    we use something like init=/bin/bash, bootloader identifier can even cause
    a crash):
    
    Kernel command line: BOOT_IMAGE=(hd0,1)/vmlinuz-6.x root=/dev/sda3 ro console=tty
    Unknown kernel command line parameters "BOOT_IMAGE=(hd0,1)/vmlinuz-6.x", will be passed to user space.
    
    [chenhuacai@loongson.cn: use strstarts()]
      Link: https://lkml.kernel.org/r/20250815090120.1569947-1-chenhuacai@loongson.cn
    Link: https://lkml.kernel.org/r/20250721101343.3283480-1-chenhuacai@loongson.cn
    Signed-off-by: Huacai Chen <chenhuacai@loongson.cn>
    Cc: Al Viro <viro@zeniv.linux.org.uk>
    Cc: Christian Brauner <brauner@kernel.org>
    Cc: Jan Kara <jack@suse.cz>
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit b62607e4f46e63157d70a899033ffcaaa77308de
Author: Sean Anderson <sean.anderson@linux.dev>
Date:   Mon Jul 14 20:28:47 2025 -0400

    iio: xilinx-ams: Unmask interrupts after updating alarms
    
    commit feb500c7ae7a198db4d2757901bce562feeefa5e upstream.
    
    To convert level-triggered alarms into edge-triggered IIO events, alarms
    are masked when they are triggered. To ensure we catch subsequent
    alarms, we then periodically poll to see if the alarm is still active.
    If it isn't, we unmask it. Active but masked alarms are stored in
    current_masked_alarm.
    
    If an active alarm is disabled, it will remain set in
    current_masked_alarm until ams_unmask_worker clears it. If the alarm is
    re-enabled before ams_unmask_worker runs, then it will never be cleared
    from current_masked_alarm. This will prevent the alarm event from being
    pushed even if the alarm is still active.
    
    Fix this by recalculating current_masked_alarm immediately when enabling
    or disabling alarms.
    
    Fixes: d5c70627a794 ("iio: adc: Add Xilinx AMS driver")
    Signed-off-by: Sean Anderson <sean.anderson@linux.dev>
    Reviewed-by: O'Griofa, Conall <conall.ogriofa@amd.com>
    Tested-by: Erim, Salih <Salih.Erim@amd.com>
    Acked-by: Erim, Salih <Salih.Erim@amd.com>
    Link: https://patch.msgid.link/20250715002847.2035228-1-sean.anderson@linux.dev
    Cc: <Stable@vger.kernel.org>
    Signed-off-by: Jonathan Cameron <Jonathan.Cameron@huawei.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit b9bf012d7b7b3d5ab58ffb24cfd58013f2330749
Author: Sean Anderson <sean.anderson@linux.dev>
Date:   Mon Jul 14 20:30:58 2025 -0400

    iio: xilinx-ams: Fix AMS_ALARM_THR_DIRECT_MASK
    
    commit 1315cc2dbd5034f566e20ddce4d675cb9e6d4ddd upstream.
    
    AMS_ALARM_THR_DIRECT_MASK should be bit 0, not bit 1. This would cause
    hysteresis to be enabled with a lower threshold of -28C. The temperature
    alarm would never deassert even if the temperature dropped below the
    upper threshold.
    
    Fixes: d5c70627a794 ("iio: adc: Add Xilinx AMS driver")
    Signed-off-by: Sean Anderson <sean.anderson@linux.dev>
    Reviewed-by: O'Griofa, Conall <conall.ogriofa@amd.com>
    Tested-by: Erim, Salih <Salih.Erim@amd.com>
    Acked-by: Erim, Salih <Salih.Erim@amd.com>
    Link: https://patch.msgid.link/20250715003058.2035656-1-sean.anderson@linux.dev
    Cc: <Stable@vger.kernel.org>
    Signed-off-by: Jonathan Cameron <Jonathan.Cameron@huawei.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit ce3922c614052b71bd37a3b372bf22798f9f6158
Author: Michael Hennerich <michael.hennerich@analog.com>
Date:   Fri Aug 29 12:25:42 2025 +0100

    iio: frequency: adf4350: Fix prescaler usage.
    
    commit 33d7ecbf69aa7dd4145e3b77962bcb8759eede3d upstream.
    
    The ADF4350/1 features a programmable dual-modulus prescaler of 4/5 or 8/9.
    When set to 4/5, the maximum RF frequency allowed is 3 GHz.
    Therefore, when operating the ADF4351 above 3 GHz, this must be set to 8/9.
    In this context not the RF output frequency is meant
    - it's the VCO frequency.
    
    Therefore move the prescaler selection after we derived the VCO frequency
    from the desired RF output frequency.
    
    This BUG may have caused PLL lock instabilities when operating the VCO at
    the very high range close to 4.4 GHz.
    
    Fixes: e31166f0fd48 ("iio: frequency: New driver for Analog Devices ADF4350/ADF4351 Wideband Synthesizers")
    Signed-off-by: Michael Hennerich <michael.hennerich@analog.com>
    Signed-off-by: Nuno Sá <nuno.sa@analog.com>
    Reviewed-by: Andy Shevchenko <andy@kernel.org>
    Link: https://patch.msgid.link/20250829-adf4350-fix-v2-1-0bf543ba797d@analog.com
    Cc: <Stable@vger.kernel.org>
    Signed-off-by: Jonathan Cameron <Jonathan.Cameron@huawei.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 2a7265a77e55435c00c07ec6a7f310e0a8305240
Author: Qianfeng Rong <rongqianfeng@vivo.com>
Date:   Mon Sep 1 21:57:26 2025 +0800

    iio: dac: ad5421: use int type to store negative error codes
    
    commit 3379c900320954d768ed9903691fb2520926bbe3 upstream.
    
    Change the 'ret' variable in ad5421_update_ctrl() from unsigned int to
    int, as it needs to store either negative error codes or zero returned
    by ad5421_write_unlocked().
    
    Fixes: 5691b23489db ("staging:iio:dac: Add AD5421 driver")
    Signed-off-by: Qianfeng Rong <rongqianfeng@vivo.com>
    Reviewed-by: Andy Shevchenko <andriy.shevchenko@intel.com>
    Link: https://patch.msgid.link/20250901135726.17601-3-rongqianfeng@vivo.com
    Cc: <Stable@vger.kernel.org>
    Signed-off-by: Jonathan Cameron <Jonathan.Cameron@huawei.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 38de3aed9780b60c0617d9b9b8ae2d30e0e309f8
Author: Qianfeng Rong <rongqianfeng@vivo.com>
Date:   Mon Sep 1 21:57:25 2025 +0800

    iio: dac: ad5360: use int type to store negative error codes
    
    commit f9381ece76de999a2065d5b4fdd87fa17883978c upstream.
    
    Change the 'ret' variable in ad5360_update_ctrl() from unsigned int to
    int, as it needs to store either negative error codes or zero returned
    by ad5360_write_unlocked().
    
    Fixes: a3e2940c24d3 ("staging:iio:dac: Add AD5360 driver")
    Signed-off-by: Qianfeng Rong <rongqianfeng@vivo.com>
    Reviewed-by: Andy Shevchenko <andriy.shevchenko@intel.com>
    Link: https://patch.msgid.link/20250901135726.17601-2-rongqianfeng@vivo.com
    Cc: <Stable@vger.kernel.org>
    Signed-off-by: Jonathan Cameron <Jonathan.Cameron@huawei.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 2dc0e5b689a4585c266d159cd6a23b4aec7b6a5f
Author: Aleksandar Gerasimovski <aleksandar.gerasimovski@belden.com>
Date:   Mon Aug 11 13:09:04 2025 +0000

    iio/adc/pac1934: fix channel disable configuration
    
    commit 3c63ba1c430af1c0dcd68dd36f2246980621dcba upstream.
    
    There are two problems with the chip configuration in this driver:
    - First, is that writing 12 bytes (ARRAY_SIZE(regs)) would anyhow
      lead to a config overflow due to HW auto increment implementation
      in the chip.
    - Second, the i2c_smbus_write_block_data write ends up in writing
      unexpected value to the channel_dis register, this is because
      the smbus size that is 0x03 in this case gets written to the
      register. The PAC1931/2/3/4 data sheet does not really specify
      that block write is indeed supported.
    
    This problem is probably not visible on PAC1934 version where all
    channels are used as the chip is properly configured by luck,
    but in our case whenusing PAC1931 this leads to nonfunctional device.
    
    Fixes: 0fb528c8255b (iio: adc: adding support for PAC193x)
    Suggested-by: Rene Straub <mailto:rene.straub@belden.com>
    Signed-off-by: Aleksandar Gerasimovski <aleksandar.gerasimovski@belden.com>
    Reviewed-by: Marius Cristea <marius.cristea@microchip.com>
    Link: https://patch.msgid.link/20250811130904.2481790-1-aleksandar.gerasimovski@belden.com
    Cc: <Stable@vger.kernel.org>
    Signed-off-by: Jonathan Cameron <Jonathan.Cameron@huawei.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit bb4142ef77b0dba7caf7a037b82a4c06675731a6
Author: Jarkko Nikula <jarkko.nikula@linux.intel.com>
Date:   Fri Sep 5 13:03:20 2025 +0300

    i3c: Fix default I2C adapter timeout value
    
    commit 9395b3c412933401a34845d5326afe4011bbd40f upstream.
    
    Commit 3a379bbcea0a ("i3c: Add core I3C infrastructure") set the default
    adapter timeout for I2C transfers as 1000 (ms). However that parameter
    is defined in jiffies not in milliseconds.
    
    With mipi-i3c-hci driver this wasn't visible until commit c0a90eb55a69
    ("i3c: mipi-i3c-hci: use adapter timeout value for I2C transfers").
    
    Fix this by setting the default timeout as HZ (CONFIG_HZ) not 1000.
    
    Fixes: 1b84691e7870 ("i3c: dw: use adapter timeout value for I2C transfers")
    Fixes: be27ed672878 ("i3c: master: cdns: use adapter timeout value for I2C transfers")
    Fixes: c0a90eb55a69 ("i3c: mipi-i3c-hci: use adapter timeout value for I2C transfers")
    Fixes: a747e01adad2 ("i3c: master: svc: use adapter timeout value for I2C transfers")
    Fixes: d028219a9f14 ("i3c: master: Add basic driver for the Renesas I3C controller")
    Fixes: 3a379bbcea0a ("i3c: Add core I3C infrastructure")
    Cc: stable@vger.kernel.org # 6.17
    Signed-off-by: Jarkko Nikula <jarkko.nikula@linux.intel.com>
    Reviewed-by: Frank Li <Frank.Li@nxp.com>
    Reviewed-by: Wolfram Sang <wsa+renesas@sang-engineering.com>
    Link: https://lore.kernel.org/r/20250905100320.954536-1-jarkko.nikula@linux.intel.com
    Signed-off-by: Alexandre Belloni <alexandre.belloni@bootlin.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit ea1ed7071a2d22af81d008dabde46d441fd3b0fd
Author: Conor Dooley <conor.dooley@microchip.com>
Date:   Thu Sep 25 16:39:18 2025 +0100

    gpio: mpfs: fix setting gpio direction to output
    
    commit bc061143637532c08d9fc657eec93fdc2588068e upstream.
    
    mpfs_gpio_direction_output() actually sets the line to input mode.
    Use the correct register settings for output mode so that this function
    actually works as intended.
    
    This was a copy-paste mistake made when converting to regmap during the
    driver submission process. It went unnoticed because my test for output
    mode is toggling LEDs on an Icicle kit which functions with the
    incorrect code. The internal reporter has yet to test the patch, but on
    their system the incorrect setting may be the reason for failures to
    drive the GPIO lines on the BeagleV-fire board.
    
    CC: stable@vger.kernel.org
    Fixes: a987b78f3615e ("gpio: mpfs: add polarfire soc gpio support")
    Signed-off-by: Conor Dooley <conor.dooley@microchip.com>
    Link: https://lore.kernel.org/r/20250925-boogieman-carrot-82989ff75d10@spud
    Signed-off-by: Bartosz Golaszewski <bartosz.golaszewski@linaro.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f19a1390af448d9e193c08e28ea5f727bf3c3049
Author: Darrick J. Wong <djwong@kernel.org>
Date:   Mon Sep 15 17:24:17 2025 -0700

    fuse: fix livelock in synchronous file put from fuseblk workers
    
    commit 26e5c67deb2e1f42a951f022fdf5b9f7eb747b01 upstream.
    
    I observed a hang when running generic/323 against a fuseblk server.
    This test opens a file, initiates a lot of AIO writes to that file
    descriptor, and closes the file descriptor before the writes complete.
    Unsurprisingly, the AIO exerciser threads are mostly stuck waiting for
    responses from the fuseblk server:
    
    # cat /proc/372265/task/372313/stack
    [<0>] request_wait_answer+0x1fe/0x2a0 [fuse]
    [<0>] __fuse_simple_request+0xd3/0x2b0 [fuse]
    [<0>] fuse_do_getattr+0xfc/0x1f0 [fuse]
    [<0>] fuse_file_read_iter+0xbe/0x1c0 [fuse]
    [<0>] aio_read+0x130/0x1e0
    [<0>] io_submit_one+0x542/0x860
    [<0>] __x64_sys_io_submit+0x98/0x1a0
    [<0>] do_syscall_64+0x37/0xf0
    [<0>] entry_SYSCALL_64_after_hwframe+0x4b/0x53
    
    But the /weird/ part is that the fuseblk server threads are waiting for
    responses from itself:
    
    # cat /proc/372210/task/372232/stack
    [<0>] request_wait_answer+0x1fe/0x2a0 [fuse]
    [<0>] __fuse_simple_request+0xd3/0x2b0 [fuse]
    [<0>] fuse_file_put+0x9a/0xd0 [fuse]
    [<0>] fuse_release+0x36/0x50 [fuse]
    [<0>] __fput+0xec/0x2b0
    [<0>] task_work_run+0x55/0x90
    [<0>] syscall_exit_to_user_mode+0xe9/0x100
    [<0>] do_syscall_64+0x43/0xf0
    [<0>] entry_SYSCALL_64_after_hwframe+0x4b/0x53
    
    The fuseblk server is fuse2fs so there's nothing all that exciting in
    the server itself.  So why is the fuse server calling fuse_file_put?
    The commit message for the fstest sheds some light on that:
    
    "By closing the file descriptor before calling io_destroy, you pretty
    much guarantee that the last put on the ioctx will be done in interrupt
    context (during I/O completion).
    
    Aha.  AIO fgets a new struct file from the fd when it queues the ioctx.
    The completion of the FUSE_WRITE command from userspace causes the fuse
    server to call the AIO completion function.  The completion puts the
    struct file, queuing a delayed fput to the fuse server task.  When the
    fuse server task returns to userspace, it has to run the delayed fput,
    which in the case of a fuseblk server, it does synchronously.
    
    Sending the FUSE_RELEASE command sychronously from fuse server threads
    is a bad idea because a client program can initiate enough simultaneous
    AIOs such that all the fuse server threads end up in delayed_fput, and
    now there aren't any threads left to handle the queued fuse commands.
    
    Fix this by only using asynchronous fputs when closing files, and leave
    a comment explaining why.
    
    Cc: stable@vger.kernel.org # v2.6.38
    Fixes: 5a18ec176c934c ("fuse: fix hang of single threaded fuseblk filesystem")
    Signed-off-by: Darrick J. Wong <djwong@kernel.org>
    Signed-off-by: Miklos Szeredi <mszeredi@redhat.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit b5f82855214bda953c809d29951f6c181518b60d
Author: Miklos Szeredi <mszeredi@redhat.com>
Date:   Mon Sep 1 17:16:26 2025 +0200

    fuse: fix possibly missing fuse_copy_finish() call in fuse_notify()
    
    commit 0b563aad1c0a05dc7d123f68a9f82f79de206dad upstream.
    
    In case of FUSE_NOTIFY_RESEND and FUSE_NOTIFY_INC_EPOCH fuse_copy_finish()
    isn't called.
    
    Fix by always calling fuse_copy_finish() after fuse_notify().  It's a no-op
    if called a second time.
    
    Fixes: 760eac73f9f6 ("fuse: Introduce a new notification type for resend pending requests")
    Fixes: 2396356a945b ("fuse: add more control over cache invalidation behaviour")
    Cc: <stable@vger.kernel.org> # v6.9
    Reviewed-by: Joanne Koong <joannelkoong@gmail.com>
    Signed-off-by: Miklos Szeredi <mszeredi@redhat.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 553bc7d4624f478f2cc2d233e5e7ffb54cf5b06d
Author: Ryan Roberts <ryan.roberts@arm.com>
Date:   Fri Oct 3 16:52:36 2025 +0100

    fsnotify: pass correct offset to fsnotify_mmap_perm()
    
    commit 28bba2c2935e219d6cb6946e16b9a0b7c47913be upstream.
    
    fsnotify_mmap_perm() requires a byte offset for the file about to be
    mmap'ed.  But it is called from vm_mmap_pgoff(), which has a page offset.
    Previously the conversion was done incorrectly so let's fix it, being
    careful not to overflow on 32-bit platforms.
    
    Discovered during code review.
    
    Link: https://lkml.kernel.org/r/20251003155238.2147410-1-ryan.roberts@arm.com
    Fixes: 066e053fe208 ("fsnotify: add pre-content hooks on mmap()")
    Signed-off-by: Ryan Roberts <ryan.roberts@arm.com>
    Reviewed-by: Kiryl Shutsemau <kas@kernel.org>
    Cc: Amir Goldstein <amir73il@gmail.com>
    Cc: David Hildenbrand <david@redhat.com>
    Cc: Liam Howlett <liam.howlett@oracle.com>
    Cc: Lorenzo Stoakes <lorenzo.stoakes@oracle.com>
    Cc: Michal Hocko <mhocko@suse.com>
    Cc: Mike Rapoport <rppt@kernel.org>
    Cc: Suren Baghdasaryan <surenb@google.com>
    Cc: Vlastimil Babka <vbabka@suse.cz>
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 8a09a62f0c8c6123c2f1864ed6d5f9eb144afaf0
Author: Shashank A P <shashank.ap@samsung.com>
Date:   Mon Sep 1 14:59:00 2025 +0530

    fs: quota: create dedicated workqueue for quota_release_work
    
    commit 72b7ceca857f38a8ca7c5629feffc63769638974 upstream.
    
    There is a kernel panic due to WARN_ONCE when panic_on_warn is set.
    
    This issue occurs when writeback is triggered due to sync call for an
    opened file(ie, writeback reason is WB_REASON_SYNC). When f2fs balance
    is needed at sync path, flush for quota_release_work is triggered.
    By default quota_release_work is queued to "events_unbound" queue which
    does not have WQ_MEM_RECLAIM flag. During f2fs balance "writeback"
    workqueue tries to flush quota_release_work causing kernel panic due to
    MEM_RECLAIM flag mismatch errors.
    
    This patch creates dedicated workqueue with WQ_MEM_RECLAIM flag
    for work quota_release_work.
    
    ------------[ cut here ]------------
    WARNING: CPU: 4 PID: 14867 at kernel/workqueue.c:3721 check_flush_dependency+0x13c/0x148
    Call trace:
     check_flush_dependency+0x13c/0x148
     __flush_work+0xd0/0x398
     flush_delayed_work+0x44/0x5c
     dquot_writeback_dquots+0x54/0x318
     f2fs_do_quota_sync+0xb8/0x1a8
     f2fs_write_checkpoint+0x3cc/0x99c
     f2fs_gc+0x190/0x750
     f2fs_balance_fs+0x110/0x168
     f2fs_write_single_data_page+0x474/0x7dc
     f2fs_write_data_pages+0x7d0/0xd0c
     do_writepages+0xe0/0x2f4
     __writeback_single_inode+0x44/0x4ac
     writeback_sb_inodes+0x30c/0x538
     wb_writeback+0xf4/0x440
     wb_workfn+0x128/0x5d4
     process_scheduled_works+0x1c4/0x45c
     worker_thread+0x32c/0x3e8
     kthread+0x11c/0x1b0
     ret_from_fork+0x10/0x20
    Kernel panic - not syncing: kernel: panic_on_warn set ...
    
    Fixes: ac6f420291b3 ("quota: flush quota_release_work upon quota writeback")
    CC: stable@vger.kernel.org
    Signed-off-by: Shashank A P <shashank.ap@samsung.com>
    Link: https://patch.msgid.link/20250901092905.2115-1-shashank.ap@samsung.com
    Signed-off-by: Jan Kara <jack@suse.cz>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 49af0d7900ed97674b6cf30b70a2ec266b48a804
Author: Haoxiang Li <haoxiang_li2024@163.com>
Date:   Tue Jul 15 17:51:20 2025 +0800

    fs/ntfs3: Fix a resource leak bug in wnd_extend()
    
    commit d68318471aa2e16222ebf492883e05a2d72b9b17 upstream.
    
    Add put_bh() to decrease the refcount of 'bh' after the job
    is finished, preventing a resource leak.
    
    Fixes: 3f3b442b5ad2 ("fs/ntfs3: Add bitmap")
    Cc: stable@vger.kernel.org
    Signed-off-by: Haoxiang Li <haoxiang_li2024@163.com>
    Signed-off-by: Konstantin Komarov <almaz.alexandrovich@paragon-software.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 7819c94b51cddb788c1d77111abecd06f0529c5a
Author: Finn Thain <fthain@linux-m68k.org>
Date:   Thu Oct 9 09:56:25 2025 +1100

    fbdev: Fix logic error in "offb" name match
    
    commit 15df28699b28d6b49dc305040c4e26a9553df07a upstream.
    
    A regression was reported to me recently whereby /dev/fb0 had disappeared
    from a PowerBook G3 Series "Wallstreet". The problem shows up when the
    "video=ofonly" parameter is passed to the kernel, which is what the
    bootloader does when "no video driver" is selected. The cause of the
    problem is the "offb" string comparison, which got mangled when it got
    refactored. Fix it.
    
    Cc: stable@vger.kernel.org
    Fixes: 93604a5ade3a ("fbdev: Handle video= parameter in video/cmdline.c")
    Reported-and-tested-by: Stan Johnson <userm57@yahoo.com>
    Signed-off-by: Finn Thain <fthain@linux-m68k.org>
    Signed-off-by: Helge Deller <deller@gmx.de>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 1325791c40fac6599990cc856ca7ee2cdd04020b
Author: Nam Cao <namcao@linutronix.de>
Date:   Tue Jul 15 14:46:34 2025 +0200

    eventpoll: Replace rwlock with spinlock
    
    commit 0c43094f8cc9d3d99d835c0ac9c4fe1ccc62babd upstream.
    
    The ready event list of an epoll object is protected by read-write
    semaphore:
    
      - The consumer (waiter) acquires the write lock and takes items.
      - the producer (waker) takes the read lock and adds items.
    
    The point of this design is enabling epoll to scale well with large number
    of producers, as multiple producers can hold the read lock at the same
    time.
    
    Unfortunately, this implementation may cause scheduling priority inversion
    problem. Suppose the consumer has higher scheduling priority than the
    producer. The consumer needs to acquire the write lock, but may be blocked
    by the producer holding the read lock. Since read-write semaphore does not
    support priority-boosting for the readers (even with CONFIG_PREEMPT_RT=y),
    we have a case of priority inversion: a higher priority consumer is blocked
    by a lower priority producer. This problem was reported in [1].
    
    Furthermore, this could also cause stall problem, as described in [2].
    
    Fix this problem by replacing rwlock with spinlock.
    
    This reduces the event bandwidth, as the producers now have to contend with
    each other for the spinlock. According to the benchmark from
    https://github.com/rouming/test-tools/blob/master/stress-epoll.c:
    
        On 12 x86 CPUs:
                      Before     After        Diff
            threads  events/ms  events/ms
                  8       7162       4956     -31%
                 16       8733       5383     -38%
                 32       7968       5572     -30%
                 64      10652       5739     -46%
                128      11236       5931     -47%
    
        On 4 riscv CPUs:
                      Before     After        Diff
            threads  events/ms  events/ms
                  8       2958       2833      -4%
                 16       3323       3097      -7%
                 32       3451       3240      -6%
                 64       3554       3178     -11%
                128       3601       3235     -10%
    
    Although the numbers look bad, it should be noted that this benchmark
    creates multiple threads who do nothing except constantly generating new
    epoll events, thus contention on the spinlock is high. For real workload,
    the event rate is likely much lower, and the performance drop is not as
    bad.
    
    Using another benchmark (perf bench epoll wait) where spinlock contention
    is lower, improvement is even observed on x86:
    
        On 12 x86 CPUs:
            Before: Averaged 110279 operations/sec (+- 1.09%), total secs = 8
            After:  Averaged 114577 operations/sec (+- 2.25%), total secs = 8
    
        On 4 riscv CPUs:
            Before: Averaged 175767 operations/sec (+- 0.62%), total secs = 8
            After:  Averaged 167396 operations/sec (+- 0.23%), total secs = 8
    
    In conclusion, no one is likely to be upset over this change. After all,
    spinlock was used originally for years, and the commit which converted to
    rwlock didn't mention a real workload, just that the benchmark numbers are
    nice.
    
    This patch is not exactly the revert of commit a218cc491420 ("epoll: use
    rwlock in order to reduce ep_poll_callback() contention"), because git
    revert conflicts in some places which are not obvious on the resolution.
    This patch is intended to be backported, therefore go with the obvious
    approach:
    
      - Replace rwlock_t with spinlock_t one to one
    
      - Delete list_add_tail_lockless() and chain_epi_lockless(). These were
        introduced to allow producers to concurrently add items to the list.
        But now that spinlock no longer allows producers to touch the event
        list concurrently, these two functions are not necessary anymore.
    
    Fixes: a218cc491420 ("epoll: use rwlock in order to reduce ep_poll_callback() contention")
    Signed-off-by: Nam Cao <namcao@linutronix.de>
    Link: https://lore.kernel.org/ec92458ea357ec503c737ead0f10b2c6e4c37d47.1752581388.git.namcao@linutronix.de
    Tested-by: K Prateek Nayak <kprateek.nayak@amd.com>
    Cc: stable@vger.kernel.org
    Reported-by: Frederic Weisbecker <frederic@kernel.org>
    Closes: https://lore.kernel.org/linux-rt-users/20210825132754.GA895675@lothringen/ [1]
    Reported-by: Valentin Schneider <vschneid@redhat.com>
    Closes: https://lore.kernel.org/linux-rt-users/xhsmhttqvnall.mognet@vschneid.remote.csb/ [2]
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit ee1c6018c6ea27b0e91a8c4a7a617bbe69eee6b4
Author: Thomas Fourier <fourier.thomas@gmail.com>
Date:   Wed Sep 3 10:06:46 2025 +0200

    crypto: rockchip - Fix dma_unmap_sg() nents value
    
    commit 21140e5caf019e4a24e1ceabcaaa16bd693b393f upstream.
    
    The dma_unmap_sg() functions should be called with the same nents as the
    dma_map_sg(), not the value the map function returned.
    
    Fixes: 57d67c6e8219 ("crypto: rockchip - rework by using crypto_engine")
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Thomas Fourier <fourier.thomas@gmail.com>
    Signed-off-by: Herbert Xu <herbert@gondor.apana.org.au>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit d0d4b7fbaaa37fac70070f71bf41839a157b636f
Author: Thomas Fourier <fourier.thomas@gmail.com>
Date:   Wed Sep 3 10:34:46 2025 +0200

    crypto: atmel - Fix dma_unmap_sg() direction
    
    commit f5d643156ef62216955c119216d2f3815bd51cb1 upstream.
    
    It seems like everywhere in this file, dd->in_sg is mapped with
    DMA_TO_DEVICE and dd->out_sg is mapped with DMA_FROM_DEVICE.
    
    Fixes: 13802005d8f2 ("crypto: atmel - add Atmel DES/TDES driver")
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Thomas Fourier <fourier.thomas@gmail.com>
    Signed-off-by: Herbert Xu <herbert@gondor.apana.org.au>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit e236c6ff835a98bcb8ad37b0d99f117e8bd0c62c
Author: Thomas Fourier <fourier.thomas@gmail.com>
Date:   Wed Sep 10 10:22:31 2025 +0200

    crypto: aspeed - Fix dma_unmap_sg() direction
    
    commit 838d2d51513e6d2504a678e906823cfd2ecaaa22 upstream.
    
    It seems like everywhere in this file, when the request is not
    bidirectionala, req->src is mapped with DMA_TO_DEVICE and req->dst is
    mapped with DMA_FROM_DEVICE.
    
    Fixes: 62f58b1637b7 ("crypto: aspeed - add HACE crypto driver")
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Thomas Fourier <fourier.thomas@gmail.com>
    Signed-off-by: Herbert Xu <herbert@gondor.apana.org.au>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 57e4a6aadf12578b96a038373cffd54b3a58b092
Author: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Date:   Fri Sep 5 15:52:03 2025 +0200

    cpufreq: intel_pstate: Fix object lifecycle issue in update_qos_request()
    
    commit 69e5d50fcf4093fb3f9f41c4f931f12c2ca8c467 upstream.
    
    The cpufreq_cpu_put() call in update_qos_request() takes place too early
    because the latter subsequently calls freq_qos_update_request() that
    indirectly accesses the policy object in question through the QoS request
    object passed to it.
    
    Fortunately, update_qos_request() is called under intel_pstate_driver_lock,
    so this issue does not matter for changing the intel_pstate operation
    mode, but it theoretically can cause a crash to occur on CPU device hot
    removal (which currently can only happen in virt, but it is formally
    supported nevertheless).
    
    Address this issue by modifying update_qos_request() to drop the
    reference to the policy later.
    
    Fixes: da5c504c7aae ("cpufreq: intel_pstate: Implement QoS supported freq constraints")
    Cc: 5.4+ <stable@vger.kernel.org> # 5.4+
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Reviewed-by: Zihuan Zhang <zhangzihuan@kylinos.cn>
    Link: https://patch.msgid.link/2255671.irdbgypaU6@rafael.j.wysocki
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 777397e7860a8f7dc654838f0139e32d54f45009
Author: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Date:   Fri Sep 26 12:19:41 2025 +0200

    cpufreq: CPPC: Avoid using CPUFREQ_ETERNAL as transition delay
    
    commit f965d111e68f4a993cc44d487d416e3d954eea11 upstream.
    
    If cppc_get_transition_latency() returns CPUFREQ_ETERNAL to indicate a
    failure to retrieve the transition latency value from the platform
    firmware, the CPPC cpufreq driver will use that value (converted to
    microseconds) as the policy transition delay, but it is way too large
    for any practical use.
    
    Address this by making the driver use the cpufreq's default
    transition latency value (in microseconds) as the transition delay
    if CPUFREQ_ETERNAL is returned by cppc_get_transition_latency().
    
    Fixes: d4f3388afd48 ("cpufreq / CPPC: Set platform specific transition_delay_us")
    Cc: 5.19+ <stable@vger.kernel.org> # 5.19
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Reviewed-by: Mario Limonciello (AMD) <superm1@kernel.org>
    Reviewed-by: Jie Zhan <zhanjie9@hisilicon.com>
    Acked-by: Viresh Kumar <viresh.kumar@linaro.org>
    Reviewed-by: Qais Yousef <qyousef@layalina.io>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit b5db860132e2c0d4132d55c2dfe8df26e280dc6e
Author: Simon Schuster <schuster.simon@siemens-energy.com>
Date:   Mon Sep 1 15:09:50 2025 +0200

    copy_sighand: Handle architectures where sizeof(unsigned long) < sizeof(u64)
    
    commit 04ff48239f46e8b493571e260bd0e6c3a6400371 upstream.
    
    With the introduction of clone3 in commit 7f192e3cd316 ("fork: add
    clone3") the effective bit width of clone_flags on all architectures was
    increased from 32-bit to 64-bit. However, the signature of the copy_*
    helper functions (e.g., copy_sighand) used by copy_process was not
    adapted.
    
    As such, they truncate the flags on any 32-bit architectures that
    supports clone3 (arc, arm, csky, m68k, microblaze, mips32, openrisc,
    parisc32, powerpc32, riscv32, x86-32 and xtensa).
    
    For copy_sighand with CLONE_CLEAR_SIGHAND being an actual u64
    constant, this triggers an observable bug in kernel selftest
    clone3_clear_sighand:
    
            if (clone_flags & CLONE_CLEAR_SIGHAND)
    
    in function copy_sighand within fork.c will always fail given:
    
            unsigned long /* == uint32_t */ clone_flags
            #define CLONE_CLEAR_SIGHAND 0x100000000ULL
    
    This commit fixes the bug by always passing clone_flags to copy_sighand
    via their declared u64 type, invariant of architecture-dependent integer
    sizes.
    
    Fixes: b612e5df4587 ("clone3: add CLONE_CLEAR_SIGHAND")
    Cc: stable@vger.kernel.org # linux-5.5+
    Signed-off-by: Simon Schuster <schuster.simon@siemens-energy.com>
    Link: https://lore.kernel.org/20250901-nios2-implement-clone3-v2-1-53fcf5577d57@siemens-energy.com
    Acked-by: David Hildenbrand <david@redhat.com>
    Reviewed-by: Lorenzo Stoakes <lorenzo.stoakes@oracle.com>
    Reviewed-by: Arnd Bergmann <arnd@arndb.de>
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a6055732eaf4360819d22720f26bebce6d645bdc
Author: Denzeel Oliva <wachiturroxd150@gmail.com>
Date:   Sat Aug 30 16:28:40 2025 +0000

    clk: samsung: exynos990: Replace bogus divs with fixed-factor clocks
    
    commit a66dabcd2cb8389fd73cab8896fd727fa2ea8d8b upstream.
    
    HSI1/2 PCIe and HSI0 USBDP debug outputs are fixed divide-by-8.
    OTP also uses 1/8 from oscclk. Replace incorrect div clocks with
    fixed-factor clocks to reflect hardware.
    
    Fixes: bdd03ebf721f ("clk: samsung: Introduce Exynos990 clock controller driver")
    Signed-off-by: Denzeel Oliva <wachiturroxd150@gmail.com>
    Cc: <stable@vger.kernel.org>
    Link: https://lore.kernel.org/r/20250830-fix-cmu-top-v5-3-7c62f608309e@gmail.com
    Signed-off-by: Krzysztof Kozlowski <krzysztof.kozlowski@linaro.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit fd9f8ed06f90fb3b11ff72c1a13f500bcfea0e7b
Author: Denzeel Oliva <wachiturroxd150@gmail.com>
Date:   Sat Aug 30 16:28:39 2025 +0000

    clk: samsung: exynos990: Fix CMU_TOP mux/div bit widths
    
    commit ce2eb09b430ddf9d7c9d685bdd81de011bccd4ad upstream.
    
    Correct several mux/div widths (DSP_BUS, G2D_MSCL, HSI0 USBDP_DEBUG,
    HSI1 UFS_EMBD, APM_BUS, CPUCL0_DBG_BUS, DPU) to match hardware.
    
    Fixes: bdd03ebf721f ("clk: samsung: Introduce Exynos990 clock controller driver")
    Signed-off-by: Denzeel Oliva <wachiturroxd150@gmail.com>
    Cc: <stable@vger.kernel.org>
    Link: https://lore.kernel.org/r/20250830-fix-cmu-top-v5-2-7c62f608309e@gmail.com
    Signed-off-by: Krzysztof Kozlowski <krzysztof.kozlowski@linaro.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit c33f4f752dec0fb241c391485ab6a1efa8daeb25
Author: Denzeel Oliva <wachiturroxd150@gmail.com>
Date:   Sat Aug 30 16:28:38 2025 +0000

    clk: samsung: exynos990: Use PLL_CON0 for PLL parent muxes
    
    commit 19b50ab02eddbbd87ec2f0ad4a5bc93ac1c9b82d upstream.
    
    Parent select bits for shared PLLs are in PLL_CON0, not PLL_CON3.
    Using the wrong register leads to incorrect parent selection and rates.
    
    Fixes: bdd03ebf721f ("clk: samsung: Introduce Exynos990 clock controller driver")
    Signed-off-by: Denzeel Oliva <wachiturroxd150@gmail.com>
    Cc: <stable@vger.kernel.org>
    Link: https://lore.kernel.org/r/20250830-fix-cmu-top-v5-1-7c62f608309e@gmail.com
    Signed-off-by: Krzysztof Kozlowski <krzysztof.kozlowski@linaro.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 52957e1810c3ac98c05836decd91fda8c7eca9ba
Author: Abel Vesa <abel.vesa@linaro.org>
Date:   Wed Jul 30 19:11:12 2025 +0300

    clk: qcom: tcsrcc-x1e80100: Set the bi_tcxo as parent to eDP refclk
    
    commit 57c8e9da3dfe606b918d8f193837ebf2213a9545 upstream.
    
    All the other ref clocks provided by this driver have the bi_tcxo
    as parent. The eDP refclk is the only one without a parent, leading
    to reporting its rate as 0. So set its parent to bi_tcxo, just like
    the rest of the refclks.
    
    Cc: stable@vger.kernel.org # v6.9
    Fixes: 06aff116199c ("clk: qcom: Add TCSR clock driver for x1e80100")
    Signed-off-by: Abel Vesa <abel.vesa@linaro.org>
    Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@oss.qualcomm.com>
    Link: https://lore.kernel.org/r/20250730-clk-qcom-tcsrcc-x1e80100-parent-edp-refclk-v1-1-7a36ef06e045@linaro.org
    Signed-off-by: Bjorn Andersson <andersson@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 10a8ac582f06225de7020f02e8efe51cf4c4f293
Author: Miaoqian Lin <linmq006@gmail.com>
Date:   Tue Sep 2 16:49:33 2025 +0800

    cdx: Fix device node reference leak in cdx_msi_domain_init
    
    commit 76254bc489d39dae9a3427f0984fe64213d20548 upstream.
    
    Add missing of_node_put() call to release
    the device node reference obtained via of_parse_phandle().
    
    Fixes: 0e439ba38e61 ("cdx: add MSI support for CDX bus")
    Cc: stable@vger.kernel.org
    Signed-off-by: Miaoqian Lin <linmq006@gmail.com>
    Acked-by: Nipun Gupta <nipun.gupta@amd.com>
    Link: https://lore.kernel.org/r/20250902084933.2418264-1-linmq006@gmail.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 94af1356ded6d049cd7c2c1a9b64026c65742d04
Author: Adam Xue <zxue@semtech.com>
Date:   Fri Sep 5 10:41:18 2025 -0700

    bus: mhi: host: Do not use uninitialized 'dev' pointer in mhi_init_irq_setup()
    
    commit d0856a6dff57f95cc5d2d74e50880f01697d0cc4 upstream.
    
    In mhi_init_irq_setup, the device pointer used for dev_err() was not
    initialized. Use the pointer from mhi_cntrl instead.
    
    Fixes: b0fc0167f254 ("bus: mhi: core: Allow shared IRQ for event rings")
    Fixes: 3000f85b8f47 ("bus: mhi: core: Add support for basic PM operations")
    Signed-off-by: Adam Xue <zxue@semtech.com>
    [mani: reworded subject/description and CCed stable]
    Signed-off-by: Manivannan Sadhasivam <manivannan.sadhasivam@oss.qualcomm.com>
    Reviewed-by: Krishna Chaitanya Chundru <krishna.chundru@oss.qualcomm.com>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250905174118.38512-1-zxue@semtech.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a43a2af63d78243c1fd43be95e3599cbe511119f
Author: Sumit Kumar <sumit.kumar@oss.qualcomm.com>
Date:   Wed Sep 10 18:11:09 2025 +0530

    bus: mhi: ep: Fix chained transfer handling in read path
    
    commit f5225a34bd8f9f64eec37f6ae1461289aaa3eb86 upstream.
    
    The mhi_ep_read_channel function incorrectly assumes the End of Transfer
    (EOT) bit is present for each packet in a chained transactions, causing
    it to advance mhi_chan->rd_offset beyond wr_offset during host-to-device
    transfers when EOT has not yet arrived. This leads to access of unmapped
    host memory, causing IOMMU faults and processing of stale TREs.
    
    Modify the loop condition to ensure mhi_queue is not empty, allowing the
    function to process only valid TREs up to the current write pointer to
    prevent premature reads and ensure safe traversal of chained TREs.
    
    Due to this change, buf_left needs to be removed from the while loop
    condition to avoid exiting prematurely before reading the ring completely,
    and also remove write_offset since it will always be zero because the new
    cache buffer is allocated every time.
    
    Fixes: 5301258899773 ("bus: mhi: ep: Add support for reading from the host")
    Co-developed-by: Akhil Vinod <akhil.vinod@oss.qualcomm.com>
    Signed-off-by: Akhil Vinod <akhil.vinod@oss.qualcomm.com>
    Signed-off-by: Sumit Kumar <sumit.kumar@oss.qualcomm.com>
    [mani: reworded description slightly]
    Signed-off-by: Manivannan Sadhasivam <manivannan.sadhasivam@oss.qualcomm.com>
    Reviewed-by: Krishna Chaitanya Chundru <krishna.chundru@oss.qualcomm.com>
    Cc: stable@vger.kernel.org
    Link: https://patch.msgid.link/20250910-final_chained-v3-1-ec77c9d88ace@oss.qualcomm.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 43143776b0a7604d873d1a6f3e552a00aa930224
Author: Anderson Nascimento <anderson@allelesecurity.com>
Date:   Mon Sep 8 09:49:02 2025 -0300

    btrfs: avoid potential out-of-bounds in btrfs_encode_fh()
    
    commit dff4f9ff5d7f289e4545cc936362e01ed3252742 upstream.
    
    The function btrfs_encode_fh() does not properly account for the three
    cases it handles.
    
    Before writing to the file handle (fh), the function only returns to the
    user BTRFS_FID_SIZE_NON_CONNECTABLE (5 dwords, 20 bytes) or
    BTRFS_FID_SIZE_CONNECTABLE (8 dwords, 32 bytes).
    
    However, when a parent exists and the root ID of the parent and the
    inode are different, the function writes BTRFS_FID_SIZE_CONNECTABLE_ROOT
    (10 dwords, 40 bytes).
    
    If *max_len is not large enough, this write goes out of bounds because
    BTRFS_FID_SIZE_CONNECTABLE_ROOT is greater than
    BTRFS_FID_SIZE_CONNECTABLE originally returned.
    
    This results in an 8-byte out-of-bounds write at
    fid->parent_root_objectid = parent_root_id.
    
    A previous attempt to fix this issue was made but was lost.
    
    https://lore.kernel.org/all/4CADAEEC020000780001B32C@vpn.id2.novell.com/
    
    Although this issue does not seem to be easily triggerable, it is a
    potential memory corruption bug that should be fixed. This patch
    resolves the issue by ensuring the function returns the appropriate size
    for all three cases and validates that *max_len is large enough before
    writing any data.
    
    Fixes: be6e8dc0ba84 ("NFS support for btrfs - v3")
    CC: stable@vger.kernel.org # 3.0+
    Signed-off-by: Anderson Nascimento <anderson@allelesecurity.com>
    Reviewed-by: David Sterba <dsterba@suse.com>
    Signed-off-by: David Sterba <dsterba@suse.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 79465347fda6fe996325b5ca6b89a2c83fbccd1f
Author: Yu Kuai <yukuai3@huawei.com>
Date:   Wed Sep 10 14:30:45 2025 +0800

    blk-crypto: fix missing blktrace bio split events
    
    commit 06d712d297649f48ebf1381d19bd24e942813b37 upstream.
    
    trace_block_split() is missing, resulting in blktrace inability to catch
    BIO split events and making it harder to analyze the BIO sequence.
    
    Cc: stable@vger.kernel.org
    Fixes: 488f6682c832 ("block: blk-crypto-fallback for Inline Encryption")
    Signed-off-by: Yu Kuai <yukuai3@huawei.com>
    Reviewed-by: Bart Van Assche <bvanassche@acm.org>
    Reviewed-by: Christoph Hellwig <hch@lst.de>
    Signed-off-by: Jens Axboe <axboe@kernel.dk>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit d4cea3ccd40119e833d79595ff9700f30d17e42e
Author: Ard Biesheuvel <ardb@kernel.org>
Date:   Thu Oct 2 23:00:45 2025 +0200

    drm/amd/display: Fix unsafe uses of kernel mode FPU
    
    commit ddbfac152830e38d488ff8e45ab7eaf5d72f8527 upstream.
    
    The point of isolating code that uses kernel mode FPU in separate
    compilation units is to ensure that even implicit uses of, e.g., SIMD
    registers for spilling occur only in a context where this is permitted,
    i.e., from inside a kernel_fpu_begin/end block.
    
    This is important on arm64, which uses -mgeneral-regs-only to build all
    kernel code, with the exception of such compilation units where FP or
    SIMD registers are expected to be used. Given that the compiler may
    invent uses of FP/SIMD anywhere in such a unit, none of its code may be
    accessible from outside a kernel_fpu_begin/end block.
    
    This means that all callers into such compilation units must use the
    DC_FP start/end macros, which must not occur there themselves. For
    robustness, all functions with external linkage that reside there should
    call dc_assert_fp_enabled() to assert that the FPU context was set up
    correctly.
    
    Fix this for the DCN35, DCN351 and DCN36 implementations.
    
    Cc: Austin Zheng <austin.zheng@amd.com>
    Cc: Jun Lei <jun.lei@amd.com>
    Cc: Harry Wentland <harry.wentland@amd.com>
    Cc: Leo Li <sunpeng.li@amd.com>
    Cc: Rodrigo Siqueira <siqueira@igalia.com>
    Cc: Alex Deucher <alexander.deucher@amd.com>
    Cc: "Christian König" <christian.koenig@amd.com>
    Cc: amd-gfx@lists.freedesktop.org
    Cc: dri-devel@lists.freedesktop.org
    Signed-off-by: Ard Biesheuvel <ardb@kernel.org>
    Signed-off-by: Alex Deucher <alexander.deucher@amd.com>
    Cc: stable@vger.kernel.org
    Signed-off-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 55673fa774ca5e339e9be522bd1dea8ffda0d64a
Author: Fangzhi Zuo <Jerry.Zuo@amd.com>
Date:   Wed Sep 24 14:37:01 2025 -0400

    drm/amd/display: Enable Dynamic DTBCLK Switch
    
    commit 5949e7c4890c3cf65e783c83c355b95e21f10dba upstream.
    
    [WHAT]
    Since dcn35, DTBCLK can be disabled when no DP2 sink connected for
    power saving purpose.
    
    Cc: Mario Limonciello <mario.limonciello@amd.com>
    Cc: Alex Deucher <alexander.deucher@amd.com>
    Cc: stable@vger.kernel.org
    Reviewed-by: Aurabindo Pillai <aurabindo.pillai@amd.com>
    Signed-off-by: Fangzhi Zuo <Jerry.Zuo@amd.com>
    Signed-off-by: Alex Hung <alex.hung@amd.com>
    Signed-off-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 8b7d49e258093527b12b143d06e8b4f87a039e68
Author: Jesse Agate <jesse.agate@amd.com>
Date:   Fri Jun 13 14:20:53 2025 -0400

    drm/amd/display: Incorrect Mirror Cositing
    
    commit d07e142641417e67f3bfc9d8ba3da8a69c39cfcd upstream.
    
    [WHY]
    hinit/vinit are incorrect in the case of mirroring.
    
    [HOW]
    Cositing sign must be flipped when image is mirrored in the vertical
    or horizontal direction.
    
    Cc: Mario Limonciello <mario.limonciello@amd.com>
    Cc: Alex Deucher <alexander.deucher@amd.com>
    Cc: stable@vger.kernel.org
    Reviewed-by: Samson Tam <samson.tam@amd.com>
    Signed-off-by: Jesse Agate <jesse.agate@amd.com>
    Signed-off-by: Brendan Leder <breleder@amd.com>
    Signed-off-by: Alex Hung <alex.hung@amd.com>
    Signed-off-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit bbe1a4a25e7e3f1675b9c234559c627f85bc0c0c
Author: Matthew Auld <matthew.auld@intel.com>
Date:   Fri Sep 19 13:20:53 2025 +0100

    drm/xe/uapi: loosen used tracking restriction
    
    commit 2d1684a077d62fddfac074052c162ec6573a34e1 upstream.
    
    Currently this is hidden behind perfmon_capable() since this is
    technically an info leak, given that this is a system wide metric.
    However the granularity reported here is always PAGE_SIZE aligned, which
    matches what the core kernel is already willing to expose to userspace
    if querying how many free RAM pages there are on the system, and that
    doesn't need any special privileges. In addition other drm drivers seem
    happy to expose this.
    
    The motivation here if with oneAPI where they want to use the system
    wide 'used' reporting here, so not the per-client fdinfo stats. This has
    also come up with some perf overlay applications wanting this
    information.
    
    Fixes: 1105ac15d2a1 ("drm/xe/uapi: restrict system wide accounting")
    Signed-off-by: Matthew Auld <matthew.auld@intel.com>
    Cc: Thomas Hellström <thomas.hellstrom@linux.intel.com>
    Cc: Joshua Santosh <joshua.santosh.ranjan@intel.com>
    Cc: José Roberto de Souza <jose.souza@intel.com>
    Cc: Matthew Brost <matthew.brost@intel.com>
    Cc: Rodrigo Vivi <rodrigo.vivi@intel.com>
    Cc: <stable@vger.kernel.org> # v6.8+
    Acked-by: Rodrigo Vivi <rodrigo.vivi@intel.com>
    Reviewed-by: Lucas De Marchi <lucas.demarchi@intel.com>
    Link: https://lore.kernel.org/r/20250919122052.420979-2-matthew.auld@intel.com
    (cherry picked from commit 4d0b035fd6dae8ee48e9c928b10f14877e595356)
    Signed-off-by: Lucas De Marchi <lucas.demarchi@intel.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 72be8bff020d717650cbd6d6cae4c0ca400629d0
Author: Shuhao Fu <sfual@cse.ust.hk>
Date:   Wed Oct 8 00:17:09 2025 +0800

    drm/nouveau: fix bad ret code in nouveau_bo_move_prep
    
    commit e4bea919584ff292c9156cf7d641a2ab3cbe27b0 upstream.
    
    In `nouveau_bo_move_prep`, if `nouveau_mem_map` fails, an error code
    should be returned. Currently, it returns zero even if vmm addr is not
    correctly mapped.
    
    Cc: stable@vger.kernel.org
    Reviewed-by: Petr Vorel <pvorel@suse.cz>
    Signed-off-by: Shuhao Fu <sfual@cse.ust.hk>
    Fixes: 9ce523cc3bf2 ("drm/nouveau: separate buffer object backing memory from nvkm structures")
    Signed-off-by: Danilo Krummrich <dakr@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 1e007e733efab09b82106ddb2c5fbebf5c58f19a
Author: Marek Vasut <marek.vasut+renesas@mailbox.org>
Date:   Wed Aug 13 23:08:13 2025 +0200

    drm/rcar-du: dsi: Fix 1/2/3 lane support
    
    commit d83f1d19c898ac1b54ae64d1c950f5beff801982 upstream.
    
    Remove fixed PPI lane count setup. The R-Car DSI host is capable
    of operating in 1..4 DSI lane mode. Remove the hard-coded 4-lane
    configuration from PPI register settings and instead configure
    the PPI lane count according to lane count information already
    obtained by this driver instance.
    
    Configure TXSETR register to match PPI lane count. The R-Car V4H
    Reference Manual R19UH0186EJ0121 Rev.1.21 section 67.2.2.3 Tx Set
    Register (TXSETR), field LANECNT description indicates that the
    TXSETR register LANECNT bitfield lane count must be configured
    such, that it matches lane count configuration in PPISETR register
    DLEN bitfield. Make sure the LANECNT and DLEN bitfields are
    configured to match.
    
    Fixes: 155358310f01 ("drm: rcar-du: Add R-Car DSI driver")
    Cc: stable@vger.kernel.org
    Signed-off-by: Marek Vasut <marek.vasut+renesas@mailbox.org>
    Reviewed-by: Tomi Valkeinen <tomi.valkeinen+renesas@ideasonboard.com>
    Link: https://lore.kernel.org/r/20250813210840.97621-1-marek.vasut+renesas@mailbox.org
    Signed-off-by: Tomi Valkeinen <tomi.valkeinen@ideasonboard.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 0b25abd9abb71ec5242d29b75c367de71f41c03a
Author: Akhil P Oommen <akhilpo@oss.qualcomm.com>
Date:   Mon Sep 8 13:56:57 2025 +0530

    drm/msm/a6xx: Fix PDC sleep sequence
    
    commit f248d5d5159a88ded55329f0b1b463d0f4094228 upstream.
    
    Since the PDC resides out of the GPU subsystem and cannot be reset in
    case it enters bad state, utmost care must be taken to trigger the PDC
    wake/sleep routines in the correct order.
    
    The PDC wake sequence can be exercised only after a PDC sleep sequence.
    Additionally, GMU firmware should initialize a few registers before the
    KMD can trigger a PDC sleep sequence. So PDC sleep can't be done if the
    GMU firmware has not initialized. Track these dependencies using a new
    status variable and trigger PDC sleep/wake sequences appropriately.
    
    Cc: stable@vger.kernel.org
    Fixes: 4b565ca5a2cb ("drm/msm: Add A6XX device support")
    Signed-off-by: Akhil P Oommen <akhilpo@oss.qualcomm.com>
    Patchwork: https://patchwork.freedesktop.org/patch/673362/
    Signed-off-by: Rob Clark <robin.clark@oss.qualcomm.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit af84271242091cc2325c3bbe93f4929a48ee42e3
Author: Jann Horn <jannh@google.com>
Date:   Wed Nov 13 22:03:39 2024 +0100

    drm/panthor: Fix memory leak in panthor_ioctl_group_create()
    
    commit ca2a6abdaee43808034cdb218428d2ed85fd3db8 upstream.
    
    When bailing out due to group_priority_permit() failure, the queue_args
    need to be freed. Fix it by rearranging the function to use the
    goto-on-error pattern, such that the success case flows straight without
    indentation while error cases jump forward to cleanup.
    
    Cc: stable@vger.kernel.org
    Fixes: 5f7762042f8a ("drm/panthor: Restrict high priorities on group_create")
    Signed-off-by: Jann Horn <jannh@google.com>
    Reviewed-by: Boris Brezillon <boris.brezillon@collabora.com>
    Reviewed-by: Liviu Dudau <liviu.dudau@arm.com>
    Reviewed-by: Steven Price <steven.price@arm.com>
    Signed-off-by: Steven Price <steven.price@arm.com>
    Link: https://lore.kernel.org/r/20241113-panthor-fix-gcq-bailout-v1-1-654307254d68@google.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 31e87afbbaef659971fcc24de3a921bd7b7a01d2
Author: Kaustabh Chakraborty <kauschluss@disroot.org>
Date:   Sun Jul 6 22:59:46 2025 +0530

    drm/exynos: exynos7_drm_decon: remove ctx->suspended
    
    commit e1361a4f1be9cb69a662c6d7b5ce218007d6e82b upstream.
    
    Condition guards are found to be redundant, as the call flow is properly
    managed now, as also observed in the Exynos5433 DECON driver. Since
    state checking is no longer necessary, remove it.
    
    This also fixes an issue which prevented decon_commit() from
    decon_atomic_enable() due to an incorrect state change setting.
    
    Fixes: 96976c3d9aff ("drm/exynos: Add DECON driver")
    Cc: stable@vger.kernel.org
    Suggested-by: Inki Dae <inki.dae@samsung.com>
    Signed-off-by: Kaustabh Chakraborty <kauschluss@disroot.org>
    Signed-off-by: Inki Dae <inki.dae@samsung.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 8178514d8cc18603c89e09875a939f4abd54ccf2
Author: Ma Ke <make24@iscas.ac.cn>
Date:   Fri Jul 18 17:50:54 2025 +0800

    media: lirc: Fix error handling in lirc_register()
    
    commit 4f4098c57e139ad972154077fb45c3e3141555dd upstream.
    
    When cdev_device_add() failed, calling put_device() to explicitly
    release dev->lirc_dev. Otherwise, it could cause the fault of the
    reference count.
    
    Found by code review.
    
    Cc: stable@vger.kernel.org
    Fixes: a6ddd4fecbb0 ("media: lirc: remove last remnants of lirc kapi")
    Signed-off-by: Ma Ke <make24@iscas.ac.cn>
    Signed-off-by: Sean Young <sean@mess.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a88e7c11093af68692daf3ac58a0f94d93989635
Author: Jai Luthra <jai.luthra@ideasonboard.com>
Date:   Mon Aug 11 13:50:15 2025 +0530

    media: ti: j721e-csi2rx: Fix source subdev link creation
    
    commit 3e743cd0a73246219da117ee99061aad51c4748c upstream.
    
    We don't use OF ports and remote-endpoints to connect the CSI2RX bridge
    and this device in the device tree, thus it is wrong to use
    v4l2_create_fwnode_links_to_pad() to create the media graph link between
    the two.
    
    It works out on accident, as neither the source nor the sink implement
    the .get_fwnode_pad() callback, and the framework helper falls back on
    using the first source and sink pads to create the link between them.
    
    Instead, manually create the media link from the first source pad of the
    bridge to the first sink pad of the J721E CSI2RX.
    
    Fixes: b4a3d877dc92 ("media: ti: Add CSI2RX support for J721E")
    Cc: stable@vger.kernel.org
    Reviewed-by: Devarsh Thakkar <devarsht@ti.com>
    Tested-by: Yemike Abhilash Chandra <y-abhilashchandra@ti.com> (on SK-AM68)
    Signed-off-by: Jai Luthra <jai.luthra@ideasonboard.com>
    Signed-off-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 6e5bdbcf41eaaae4fe0f43c5c633622ceb0f9435
Author: Jai Luthra <jai.luthra@ideasonboard.com>
Date:   Mon Aug 11 13:50:13 2025 +0530

    media: ti: j721e-csi2rx: Use devm_of_platform_populate
    
    commit 072799db233f9de90a62be54c1e59275c2db3969 upstream.
    
    Ensure that we clean up the platform bus when we remove this driver.
    
    This fixes a crash seen when reloading the module for the child device
    with the parent not yet reloaded.
    
    Fixes: b4a3d877dc92 ("media: ti: Add CSI2RX support for J721E")
    Cc: stable@vger.kernel.org
    Reviewed-by: Devarsh Thakkar <devarsht@ti.com>
    Tested-by: Yemike Abhilash Chandra <y-abhilashchandra@ti.com> (on SK-AM68)
    Signed-off-by: Jai Luthra <jai.luthra@ideasonboard.com>
    Signed-off-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit b3c08b582dcfb77d77f7003c1985e6ab37e2b794
Author: Laurent Pinchart <laurent.pinchart+renesas@ideasonboard.com>
Date:   Thu Aug 21 18:42:41 2025 +0300

    media: vsp1: Export missing vsp1_isp_free_buffer symbol
    
    commit b32655a5f4c1a3b830f05fe3d43e17b2c4d09146 upstream.
    
    The vsp1_isp_free_buffer() function implemented by the vsp1 driver is
    part of the API exposed to the rcar-isp driver. All other symbols except
    that one are properly exported. Fix it.
    
    Fixes: d06c1a9f348d ("media: vsp1: Add VSPX support")
    Cc: stable@vger.kernel.org
    Signed-off-by: Laurent Pinchart <laurent.pinchart+renesas@ideasonboard.com>
    Reviewed-by: Jacopo Mondi <jacopo.mondi@ideasonboard.com>
    Reviewed-by: Niklas Söderlund <niklas.soderlund+renesas@ragnatech.se>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 9cdf37199432ae22104c6803baf3a0ef536c9ddb
Author: Hans Verkuil <hverkuil+cisco@kernel.org>
Date:   Sat Sep 6 12:11:21 2025 +0200

    media: vivid: fix disappearing <Vendor Command With ID> messages
    
    commit 4bd8a6147645480d550242ff816b4c7ba160e5b7 upstream.
    
    The vivid driver supports the <Vendor Command With ID> message,
    but if the Vendor ID of the received message didn't match the Vendor ID
    of the CEC Adapter, then it ignores it (good) and returns 0 (bad).
    
    It should return -ENOMSG to indicate that other followers should be
    asked to handle it. Return code 0 means that the driver handled it,
    which is wrong in this case.
    
    As a result, userspace followers never get the chance to process such a
    message.
    
    Refactor the code a bit to have the function return -ENOMSG at the end,
    drop the default case, and ensure that the message handlers return 0.
    
    That way 0 is only returned if the message is actually handled in the
    vivid_received() function.
    
    Fixes: 812765cd6954 ("media: vivid: add <Vendor Command With ID> support")
    Cc: stable@vger.kernel.org
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Mauro Carvalho Chehab <mchehab+huawei@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f48b72d72c38f53531e485cb6f0ab9ef2db0df5c
Author: Renjiang Han <quic_renjiang@quicinc.com>
Date:   Thu Sep 18 17:31:08 2025 +0530

    media: venus: pm_helpers: add fallback for the opp-table
    
    commit afb100a5ea7a13d7e6937dcd3b36b19dc6cc9328 upstream.
    
    Since the device trees for both HFI_VERSION_1XX and HFI_VERSION_3XX
    do not include an opp-table and have not configured opp-pmdomain, they
    still need to use the frequencies defined in the driver's freq_tbl.
    
    Both core_power_v1 and core_power_v4 functions require core_clks_enable
    function during POWER_ON. Therefore, in the core_clks_enable function,
    if calling dev_pm_opp_find_freq_ceil to obtain the frequency fails,
    it needs to fall back to the freq_tbl to retrieve the frequency.
    
    Fixes: b179234b5e59 ("media: venus: pm_helpers: use opp-table for the frequency")
    Cc: stable@vger.kernel.org
    Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@oss.qualcomm.com>
    Reviewed-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org>
    Reviewed-by: Vikash Garodia <quic_vgarodia@quicinc.com>
    Closes: https://lore.kernel.org/linux-media/CA+G9fYu5=3n84VY+vTbCAcfFKOq7Us5vgBZgpypY4MveM=eVwg@mail.gmail.com
    Signed-off-by: Renjiang Han <quic_renjiang@quicinc.com>
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a1362af5ac29bd67b2c8d7341fd89d02bb389f1f
Author: Stephan Gerhold <stephan.gerhold@linaro.org>
Date:   Wed Aug 20 17:16:39 2025 +0200

    media: venus: firmware: Use correct reset sequence for IRIS2
    
    commit 93f213b444a40f1e7a4383b499b65e782dcb14b9 upstream.
    
    When starting venus with the "no_tz" code path, IRIS2 needs the same
    boot/reset sequence as IRIS2_1. This is because most of the registers were
    moved to the "wrapper_tz_base", which is already defined for both IRIS2 and
    IRIS2_1 inside core.c. Add IRIS2 to the checks inside firmware.c as well to
    make sure that it uses the correct reset sequence.
    
    Both IRIS2 and IRIS2_1 are HFI v6 variants, so the correct sequence was
    used before commit c38610f8981e ("media: venus: firmware: Sanitize
    per-VPU-version").
    
    Fixes: c38610f8981e ("media: venus: firmware: Sanitize per-VPU-version")
    Cc: stable@vger.kernel.org
    Signed-off-by: Stephan Gerhold <stephan.gerhold@linaro.org>
    Reviewed-by: Vikash Garodia <quic_vgarodia@quicinc.com>
    Reviewed-by: Dikshita Agarwal <quic_dikshita@quicinc.com>
    Reviewed-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org>
    Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@oss.qualcomm.com>
    [bod: Fixed commit log IRIS -> IRIS2]
    Signed-off-by: Bryan O'Donoghue <bod@kernel.org>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit daca6e22acc3d19805979097f5ca1b4bda042c16
Author: Desnes Nunes <desnesn@redhat.com>
Date:   Tue Jul 8 11:46:28 2025 -0300

    media: uvcvideo: Avoid variable shadowing in uvc_ctrl_cleanup_fh
    
    commit f4da0de6b4b470a60c5c0cc4c09b0c987f9df35f upstream.
    
    This avoids a variable loop shadowing occurring between the local loop
    iterating through the uvc_entity's controls and the global one going
    through the pending async controls of the file handle.
    
    Fixes: 10acb9101355 ("media: uvcvideo: Increase/decrease the PM counter per IOCTL")
    Cc: stable@vger.kernel.org
    Signed-off-by: Desnes Nunes <desnesn@redhat.com>
    Reviewed-by: Laurent Pinchart <laurent.pinchart@ideasonboard.com>
    Signed-off-by: Hans de Goede <hansg@kernel.org>
    Signed-off-by: Laurent Pinchart <laurent.pinchart@ideasonboard.com>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit cf7bd54b309ce4c37d79bb02f2f26b85c7a80bc7
Author: Bingbu Cao <bingbu.cao@intel.com>
Date:   Tue Sep 9 14:01:53 2025 +0800

    media: staging/ipu7: fix isys device runtime PM usage in firmware closing
    
    commit 895d3b4b5832edefd2f1fbad9d75c0179f47fe0e upstream.
    
    The PM usage counter of isys was bumped up when start camera stream
    (opening firmware) but it was not dropped after stream stop(closing
    firmware), it forbids system fail to suspend due to the wrong PM state
    of ISYS. This patch drop the PM usage counter in firmware close to fix
    it.
    
    Cc: Stable@vger.kernel.org
    Fixes: a516d36bdc3d ("media: staging/ipu7: add IPU7 input system device driver")
    Signed-off-by: Bingbu Cao <bingbu.cao@intel.com>
    Signed-off-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 74f73990073631f997353fcbd88d4e43c05b8d18
Author: Arnd Bergmann <arnd@arndb.de>
Date:   Thu Aug 7 22:54:15 2025 +0200

    media: s5p-mfc: remove an unused/uninitialized variable
    
    commit 7fa37ba25a1dfc084e24ea9acc14bf1fad8af14c upstream.
    
    The s5p_mfc_cmd_args structure in the v6 driver is never used, not
    initialized to anything other than zero, but as of clang-21 this
    causes a warning:
    
    drivers/media/platform/samsung/s5p-mfc/s5p_mfc_cmd_v6.c:45:7: error: variable 'h2r_args' is uninitialized when passed as a const pointer argument here [-Werror,-Wuninitialized-const-pointer]
       45 |                                         &h2r_args);
          |                                          ^~~~~~~~
    
    Just remove this for simplicity. Since the function is also called
    through a callback, this does require adding a trivial wrapper with
    the correct prototype.
    
    Fixes: f96f3cfa0bb8 ("[media] s5p-mfc: Update MFC v4l2 driver to support MFC6.x")
    Cc: stable@vger.kernel.org
    Signed-off-by: Arnd Bergmann <arnd@arndb.de>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a84ce98a075629040fbd24a0dcb05fa9d391c5ab
Author: Nícolas F. R. A. Prado <nfraprado@collabora.com>
Date:   Fri Jun 6 09:14:22 2025 -0400

    media: platform: mtk-mdp3: Add missing MT8188 compatible to comp_dt_ids
    
    commit bbcc6d16dea4b5c878d56a8d25daf996c6b8a1d4 upstream.
    
    Commit 4a81656c8eaa ("arm64: dts: mediatek: mt8188: Address binding
    warnings for MDP3 nodes") caused a regression on the MDP functionality
    when it removed the MT8195 compatibles from the MDP3 nodes, since the
    MT8188 compatible was not yet listed as a possible MDP component
    compatible in mdp_comp_dt_ids. This resulted in an empty output
    bitstream when using the MDP from userspace, as well as the following
    errors:
    
      mtk-mdp3 14001000.dma-controller: Uninit component inner id 4
      mtk-mdp3 14001000.dma-controller: mdp_path_ctx_init error 0
      mtk-mdp3 14001000.dma-controller: CMDQ sendtask failed: -22
    
    Add the missing compatible to the array to restore functionality.
    
    Fixes: 4a81656c8eaa ("arm64: dts: mediatek: mt8188: Address binding warnings for MDP3 nodes")
    Cc: stable@vger.kernel.org
    Signed-off-by: Nícolas F. R. A. Prado <nfraprado@collabora.com>
    Signed-off-by: Nicolas Dufresne <nicolas.dufresne@collabora.com>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit b792eba44494b4e6ab5006013335f9819f303b8b
Author: David Lechner <dlechner@baylibre.com>
Date:   Tue Jul 22 17:05:46 2025 -0500

    media: pci: mg4b: fix uninitialized iio scan data
    
    commit c0d3f6969bb4d72476cfe7ea9263831f1c283704 upstream.
    
    Fix potential leak of uninitialized stack data to userspace by ensuring
    that the `scan` structure is zeroed before use.
    
    Fixes: 0ab13674a9bd ("media: pci: mgb4: Added Digiteq Automotive MGB4 driver")
    Cc: stable@vger.kernel.org
    Signed-off-by: David Lechner <dlechner@baylibre.com>
    Reviewed-by: Jonathan Cameron <jonathan.cameron@huawei.com>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 2f6aa32aaf4e1d54ef73773e2d263102e50dee75
Author: Thomas Fourier <fourier.thomas@gmail.com>
Date:   Wed Jul 16 15:26:30 2025 +0200

    media: pci: ivtv: Add missing check after DMA map
    
    commit 1069a4fe637d0e3e4c163e3f8df9be306cc299b4 upstream.
    
    The DMA map functions can fail and should be tested for errors.
    If the mapping fails, free blanking_ptr and set it to 0.  As 0 is a
    valid DMA address, use blanking_ptr to test if the DMA address
    is set.
    
    Fixes: 1a0adaf37c30 ("V4L/DVB (5345): ivtv driver for Conexant cx23416/cx23415 MPEG encoder/decoder")
    Cc: stable@vger.kernel.org
    Signed-off-by: Thomas Fourier <fourier.thomas@gmail.com>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 7a9994d46cbb2d7410229debeae91718eaa02eef
Author: Laurent Pinchart <laurent.pinchart@ideasonboard.com>
Date:   Wed Aug 20 17:00:20 2025 +0300

    media: mc: Fix MUST_CONNECT handling for pads with no links
    
    commit eec81250219a209b863f11d02128ec1dd8e20877 upstream.
    
    Commit b3decc5ce7d7 ("media: mc: Expand MUST_CONNECT flag to always
    require an enabled link") expanded the meaning of the MUST_CONNECT flag
    to require an enabled link in all cases. To do so, the link exploration
    code was expanded to cover unconnected pads, in order to reject those
    that have the MUST_CONNECT flag set. The implementation was however
    incorrect, ignoring unconnected pads instead of ignoring connected pads.
    Fix it.
    
    Reported-by: Martin Kepplinger-Novaković <martink@posteo.de>
    Closes: https://lore.kernel.org/linux-media/20250205172957.182362-1-martink@posteo.de
    Reported-by: Maud Spierings <maudspierings@gocontroll.com>
    Closes: https://lore.kernel.org/linux-media/20250818-imx8_isi-v1-1-e9cfe994c435@gocontroll.com
    Fixes: b3decc5ce7d7 ("media: mc: Expand MUST_CONNECT flag to always require an enabled link")
    Cc: stable@vger.kernel.org # 6.1
    Signed-off-by: Laurent Pinchart <laurent.pinchart@ideasonboard.com>
    Tested-by: Maud Spierings <maudspierings@gocontroll.com>
    Tested-by: Martin Kepplinger-Novaković <martink@posteo.de>
    Signed-off-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit dd4a438b92e3fbc9008482ff3450f45922274de1
Author: Qianfeng Rong <rongqianfeng@vivo.com>
Date:   Wed Aug 27 20:39:10 2025 +0800

    media: i2c: mt9v111: fix incorrect type for ret
    
    commit bacd713145443dce7764bb2967d30832a95e5ec8 upstream.
    
    Change "ret" from unsigned int to int type in mt9v111_calc_frame_rate()
    to store negative error codes or zero returned by __mt9v111_hw_reset()
    and other functions.
    
    Storing the negative error codes in unsigned type, doesn't cause an issue
    at runtime but it's ugly as pants.
    
    No effect on runtime.
    
    Signed-off-by: Qianfeng Rong <rongqianfeng@vivo.com>
    Fixes: aab7ed1c3927 ("media: i2c: Add driver for Aptina MT9V111")
    Cc: stable@vger.kernel.org
    Reviewed-by: Jacopo Mondi <jacopo.mondi@ideasonboard.com>
    Signed-off-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 7d52be220d45620672d9b823f890d38016e5091c
Author: Hans Verkuil <hverkuil+cisco@kernel.org>
Date:   Thu Apr 24 11:27:30 2025 +0200

    media: i2c: mt9p031: fix mbus code initialization
    
    commit 075710b670d96cf9edca1894abecba7402fe4f34 upstream.
    
    The mediabus code is device dependent, but the probe() function
    thought that device_get_match_data() would return the code directly,
    when in fact it returned a pointer to a struct mt9p031_model_info.
    
    As a result, the initial mbus code was garbage.
    
    Tested with a BeagleBoard xM and a Leopard Imaging LI-5M03 sensor board.
    
    Signed-off-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Tested-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Fixes: a80b1bbff88b ("media: mt9p031: Refactor format handling for different sensor models")
    Cc: stable@vger.kernel.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 4fd9c22c2b21a248f0cabd2556e766e31493c230
Author: Thomas Fourier <fourier.thomas@gmail.com>
Date:   Wed Jul 9 13:35:40 2025 +0200

    media: cx18: Add missing check after DMA map
    
    commit 23b53639a793477326fd57ed103823a8ab63084f upstream.
    
    The DMA map functions can fail and should be tested for errors.
    If the mapping fails, dealloc buffers, and return.
    
    Fixes: 1c1e45d17b66 ("V4L/DVB (7786): cx18: new driver for the Conexant CX23418 MPEG encoder chip")
    Cc: stable@vger.kernel.org
    Signed-off-by: Thomas Fourier <fourier.thomas@gmail.com>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 0c8316cfc64dc80d505d91f38104ec5e431a4961
Author: Randy Dunlap <rdunlap@infradead.org>
Date:   Tue Jul 22 17:12:00 2025 -0700

    media: cec: extron-da-hd-4k-plus: drop external-module make commands
    
    commit d5d12cc03e501c38925e544abe44d5bfe23dc930 upstream.
    
    Delete the external-module style Makefile commands. They are not needed
    for in-tree modules.
    
    This is the only Makefile in the kernel tree (aside from tools/ and
    samples/) that uses this Makefile style.
    
    The same files are built with or without this patch.
    
    Fixes: 056f2821b631 ("media: cec: extron-da-hd-4k-plus: add the Extron DA HD 4K Plus CEC driver")
    Signed-off-by: Randy Dunlap <rdunlap@infradead.org>
    Cc: stable@vger.kernel.org
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 6afea664e913488b51f9961f6437011385d6a5aa
Author: Johan Hovold <johan@kernel.org>
Date:   Fri Jul 25 09:40:19 2025 +0200

    firmware: meson_sm: fix device leak at probe
    
    commit 8ece3173f87df03935906d0c612c2aeda9db92ca upstream.
    
    Make sure to drop the reference to the secure monitor device taken by
    of_find_device_by_node() when looking up its driver data on behalf of
    other drivers (e.g. during probe).
    
    Note that holding a reference to the platform device does not prevent
    its driver data from going away so there is no point in keeping the
    reference after the helper returns.
    
    Fixes: 8cde3c2153e8 ("firmware: meson_sm: Rework driver as a proper platform driver")
    Cc: stable@vger.kernel.org      # 5.5
    Cc: Carlo Caione <ccaione@baylibre.com>
    Signed-off-by: Johan Hovold <johan@kernel.org>
    Acked-by: Martin Blumenstingl <martin.blumenstingl@googlemail.com>
    Link: https://lore.kernel.org/r/20250725074019.8765-1-johan@kernel.org
    Signed-off-by: Neil Armstrong <neil.armstrong@linaro.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 9a5aad7d6e1d3ca640f6a9ab94c130eaa5c496b4
Author: Tudor Ambarus <tudor.ambarus@linaro.org>
Date:   Mon Sep 8 14:02:00 2025 +0000

    firmware: exynos-acpm: fix PMIC returned errno
    
    commit 1da4cbefed4a2e69ebad81fc9b356cd9b807f380 upstream.
    
    ACPM PMIC command handlers returned a u8 value when they should
    have returned either zero or negative error codes.
    Translate the APM PMIC errno to linux errno.
    
    Reported-by: Dan Carpenter <dan.carpenter@linaro.org>
    Closes: https://lore.kernel.org/linux-input/aElHlTApXj-W_o1r@stanley.mountain/
    Fixes: a88927b534ba ("firmware: add Exynos ACPM protocol driver")
    Cc: stable@vger.kernel.org
    Signed-off-by: Tudor Ambarus <tudor.ambarus@linaro.org>
    Signed-off-by: Krzysztof Kozlowski <krzysztof.kozlowski@linaro.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 61c07f0dccb662e944c00f86c53cfafe0691aa28
Author: Jason Andryuk <jason.andryuk@amd.com>
Date:   Wed Aug 27 20:36:03 2025 -0400

    xen/events: Update virq_to_irq on migration
    
    commit 3fcc8e146935415d69ffabb5df40ecf50e106131 upstream.
    
    VIRQs come in 3 flavors, per-VPU, per-domain, and global, and the VIRQs
    are tracked in per-cpu virq_to_irq arrays.
    
    Per-domain and global VIRQs must be bound on CPU 0, and
    bind_virq_to_irq() sets the per_cpu virq_to_irq at registration time
    Later, the interrupt can migrate, and info->cpu is updated.  When
    calling __unbind_from_irq(), the per-cpu virq_to_irq is cleared for a
    different cpu.  If bind_virq_to_irq() is called again with CPU 0, the
    stale irq is returned.  There won't be any irq_info for the irq, so
    things break.
    
    Make xen_rebind_evtchn_to_cpu() update the per_cpu virq_to_irq mappings
    to keep them update to date with the current cpu.  This ensures the
    correct virq_to_irq is cleared in __unbind_from_irq().
    
    Fixes: e46cdb66c8fc ("xen: event channels")
    Cc: stable@vger.kernel.org
    Signed-off-by: Jason Andryuk <jason.andryuk@amd.com>
    Reviewed-by: Juergen Gross <jgross@suse.com>
    Signed-off-by: Juergen Gross <jgross@suse.com>
    Message-ID: <20250828003604.8949-4-jason.andryuk@amd.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f81db055a793eca9d05f79658ff62adafb41d664
Author: Jason Andryuk <jason.andryuk@amd.com>
Date:   Wed Aug 27 20:36:02 2025 -0400

    xen/events: Return -EEXIST for bound VIRQs
    
    commit 07ce121d93a5e5fb2440a24da3dbf408fcee978e upstream.
    
    Change find_virq() to return -EEXIST when a VIRQ is bound to a
    different CPU than the one passed in.  With that, remove the BUG_ON()
    from bind_virq_to_irq() to propogate the error upwards.
    
    Some VIRQs are per-cpu, but others are per-domain or global.  Those must
    be bound to CPU0 and can then migrate elsewhere.  The lookup for
    per-domain and global will probably fail when migrated off CPU 0,
    especially when the current CPU is tracked.  This now returns -EEXIST
    instead of BUG_ON().
    
    A second call to bind a per-domain or global VIRQ is not expected, but
    make it non-fatal to avoid trying to look up the irq, since we don't
    know which per_cpu(virq_to_irq) it will be in.
    
    Cc: stable@vger.kernel.org
    Signed-off-by: Jason Andryuk <jason.andryuk@amd.com>
    Reviewed-by: Juergen Gross <jgross@suse.com>
    Signed-off-by: Juergen Gross <jgross@suse.com>
    Message-ID: <20250828003604.8949-3-jason.andryuk@amd.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 9f2c55afc945a7178aa14fd021cf50b76b34c8c7
Author: Lukas Wunner <lukas@wunner.de>
Date:   Thu Sep 4 15:11:09 2025 +0200

    xen/manage: Fix suspend error path
    
    commit f770c3d858687252f1270265ba152d5c622e793f upstream.
    
    The device power management API has the following asymmetry:
    * dpm_suspend_start() does not clean up on failure
      (it requires a call to dpm_resume_end())
    * dpm_suspend_end() does clean up on failure
      (it does not require a call to dpm_resume_start())
    
    The asymmetry was introduced by commit d8f3de0d2412 ("Suspend-related
    patches for 2.6.27") in June 2008:  It removed a call to device_resume()
    from device_suspend() (which was later renamed to dpm_suspend_start()).
    
    When Xen began using the device power management API in May 2008 with
    commit 0e91398f2a5d ("xen: implement save/restore"), the asymmetry did
    not yet exist.  But since it was introduced, a call to dpm_resume_end()
    is missing in the error path of dpm_suspend_start().  Fix it.
    
    Fixes: d8f3de0d2412 ("Suspend-related patches for 2.6.27")
    Signed-off-by: Lukas Wunner <lukas@wunner.de>
    Cc: stable@vger.kernel.org  # v2.6.27
    Reviewed-by: "Rafael J. Wysocki (Intel)" <rafael@kernel.org>
    Signed-off-by: Juergen Gross <jgross@suse.com>
    Message-ID: <22453676d1ddcebbe81641bb68ddf587fee7e21e.1756990799.git.lukas@wunner.de>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 1b222eb008e3b918c152c84166c6cc5c575dfb1d
Author: Jason Andryuk <jason.andryuk@amd.com>
Date:   Wed Aug 27 20:36:01 2025 -0400

    xen/events: Cleanup find_virq() return codes
    
    commit 08df2d7dd4ab2db8a172d824cda7872d5eca460a upstream.
    
    rc is overwritten by the evtchn_status hypercall in each iteration, so
    the return value will be whatever the last iteration is.  This could
    incorrectly return success even if the event channel was not found.
    Change to an explicit -ENOENT for an un-found virq and return 0 on a
    successful match.
    
    Fixes: 62cc5fc7b2e0 ("xen/pv-on-hvm kexec: rebind virqs to existing eventchannel ports")
    Cc: stable@vger.kernel.org
    Signed-off-by: Jason Andryuk <jason.andryuk@amd.com>
    Reviewed-by: Jan Beulich <jbeulich@suse.com>
    Reviewed-by: Juergen Gross <jgross@suse.com>
    Signed-off-by: Juergen Gross <jgross@suse.com>
    Message-ID: <20250828003604.8949-2-jason.andryuk@amd.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a811dbc88ff7846ad2fde9e17316ae562a6683e3
Author: Marek Marczykowski-Górecki <marmarek@invisiblethingslab.com>
Date:   Sun Sep 21 18:28:47 2025 +0200

    xen: take system_transition_mutex on suspend
    
    commit 9d52b0b41be5b932a0a929c10038f1bb04af4ca5 upstream.
    
    Xen's do_suspend() calls dpm_suspend_start() without taking required
    system_transition_mutex. Since 12ffc3b1513eb moved the
    pm_restrict_gfp_mask() call, not taking that mutex results in a WARN.
    
    Take the mutex in do_suspend(), and use mutex_trylock() to follow
    how enter_state() does this.
    
    Suggested-by: Jürgen Groß <jgross@suse.com>
    Fixes: 12ffc3b1513eb "PM: Restrict swap use to later in the suspend sequence"
    Link: https://lore.kernel.org/xen-devel/aKiBJeqsYx_4Top5@mail-itl/
    Signed-off-by: Marek Marczykowski-Górecki <marmarek@invisiblethingslab.com>
    Cc: stable@vger.kernel.org # v6.16+
    Reviewed-by: Juergen Gross <jgross@suse.com>
    Signed-off-by: Juergen Gross <jgross@suse.com>
    Message-ID: <20250921162853.223116-1-marmarek@invisiblethingslab.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 2b51fa1f7996376335f8f4ee8624cb0fdb80d9dc
Author: Michael Riesch <michael.riesch@collabora.com>
Date:   Wed Sep 3 19:04:50 2025 +0200

    dt-bindings: phy: rockchip-inno-csi-dphy: make power-domains non-required
    
    commit c254815b02673cc77a84103c4c0d6197bd90c0ef upstream.
    
    There are variants of the Rockchip Innosilicon CSI DPHY (e.g., the RK3568
    variant) that are powered on by default as they are part of the ALIVE power
    domain.
    Remove 'power-domains' from the required properties in order to avoid false
    positives.
    
    Fixes: 22c8e0a69b7f ("dt-bindings: phy: add compatible for rk356x to rockchip-inno-csi-dphy")
    Cc: stable@kernel.org
    Reviewed-by: Krzysztof Kozlowski <krzysztof.kozlowski@linaro.org>
    Signed-off-by: Michael Riesch <michael.riesch@collabora.com>
    Link: https://lore.kernel.org/r/20250616-rk3588-csi-dphy-v4-2-a4f340a7f0cf@collabora.com
    Signed-off-by: Vinod Koul <vkoul@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 1156d54f7f79df9157e6c06d17118df0e9be974e
Author: Tony Lindgren <tony.lindgren@linux.intel.com>
Date:   Thu Sep 18 08:32:25 2025 +0300

    KVM: TDX: Fix uninitialized error code for __tdx_bringup()
    
    commit 510c47f165f0c1f0b57329a30a9a797795519831 upstream.
    
    Fix a Smatch static checker warning reported by Dan:
    
            arch/x86/kvm/vmx/tdx.c:3464 __tdx_bringup()
            warn: missing error code 'r'
    
    Initialize r to -EINVAL before tdx_get_sysinfo() to simplify the code and
    to prevent similar issues from sneaking in later on as suggested by Kai.
    
    Cc: stable@vger.kernel.org
    Reported-by: Dan Carpenter <dan.carpenter@linaro.org>
    Fixes: 61bb28279623 ("KVM: TDX: Get system-wide info about TDX module on initialization")
    Suggested-by: Kai Huang <kai.huang@intel.com>
    Reviewed-by: Kai Huang <kai.huang@intel.com>
    Signed-off-by: Tony Lindgren <tony.lindgren@linux.intel.com>
    Link: https://lore.kernel.org/r/20250918053226.802204-1-tony.lindgren@linux.intel.com
    [sean: tag for stable]
    Signed-off-by: Sean Christopherson <seanjc@google.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit cc52ee3195c3dd0b8801df81bc44ec3e436c1562
Author: Hou Wenlong <houwenlong.hwl@antgroup.com>
Date:   Tue Sep 23 08:37:38 2025 -0700

    KVM: SVM: Re-load current, not host, TSC_AUX on #VMEXIT from SEV-ES guest
    
    commit 29da8c823abffdacb71c7c07ec48fcf9eb38757c upstream.
    
    Prior to running an SEV-ES guest, set TSC_AUX in the host save area to the
    current value in hardware, as tracked by the user return infrastructure,
    instead of always loading the host's desired value for the CPU.  If the
    pCPU is also running a non-SEV-ES vCPU, loading the host's value on #VMEXIT
    could clobber the other vCPU's value, e.g. if the SEV-ES vCPU preempted
    the non-SEV-ES vCPU, in which case KVM expects the other vCPU's TSC_AUX
    value to be resident in hardware.
    
    Note, unlike TDX, which blindly _zeroes_ TSC_AUX on TD-Exit, SEV-ES CPUs
    can load an arbitrary value.  Stuff the current value in the host save
    area instead of refreshing the user return cache so that KVM doesn't need
    to track whether or not the vCPU actually enterred the guest and thus
    loaded TSC_AUX from the host save area.
    
    Opportunistically tag tsc_aux_uret_slot as read-only after init to guard
    against unexpected modifications, and to make it obvious that using the
    variable in sev_es_prepare_switch_to_guest() is safe.
    
    Fixes: 916e3e5f26ab ("KVM: SVM: Do not use user return MSR support for virtualized TSC_AUX")
    Cc: stable@vger.kernel.org
    Suggested-by: Lai Jiangshan <jiangshan.ljs@antgroup.com>
    Signed-off-by: Hou Wenlong <houwenlong.hwl@antgroup.com>
    [sean: handle the SEV-ES case in sev_es_prepare_switch_to_guest()]
    Reviewed-by: Xiaoyao Li <xiaoyao.li@intel.com>
    Link: https://lore.kernel.org/r/20250923153738.1875174-3-seanjc@google.com
    Signed-off-by: Sean Christopherson <seanjc@google.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 91ab8a21bda2d2d2842b6159ac060d9100433a3c
Author: Sean Christopherson <seanjc@google.com>
Date:   Wed Aug 27 17:52:49 2025 -0700

    x86/kvm: Force legacy PCI hole to UC when overriding MTRRs for TDX/SNP
    
    commit 0dccbc75e18df85399a71933d60b97494110f559 upstream.
    
    When running as an SNP or TDX guest under KVM, force the legacy PCI hole,
    i.e. memory between Top of Lower Usable DRAM and 4GiB, to be mapped as UC
    via a forced variable MTRR range.
    
    In most KVM-based setups, legacy devices such as the HPET and TPM are
    enumerated via ACPI.  ACPI enumeration includes a Memory32Fixed entry, and
    optionally a SystemMemory descriptor for an OperationRegion, e.g. if the
    device needs to be accessed via a Control Method.
    
    If a SystemMemory entry is present, then the kernel's ACPI driver will
    auto-ioremap the region so that it can be accessed at will.  However, the
    ACPI spec doesn't provide a way to enumerate the memory type of
    SystemMemory regions, i.e. there's no way to tell software that a region
    must be mapped as UC vs. WB, etc.  As a result, Linux's ACPI driver always
    maps SystemMemory regions using ioremap_cache(), i.e. as WB on x86.
    
    The dedicated device drivers however, e.g. the HPET driver and TPM driver,
    want to map their associated memory as UC or WC, as accessing PCI devices
    using WB is unsupported.
    
    On bare metal and non-CoCO, the conflicting requirements "work" as firmware
    configures the PCI hole (and other device memory) to be UC in the MTRRs.
    So even though the ACPI mappings request WB, they are forced to UC- in the
    kernel's tracking due to the kernel properly handling the MTRR overrides,
    and thus are compatible with the drivers' requested WC/UC-.
    
    With force WB MTRRs on SNP and TDX guests, the ACPI mappings get their
    requested WB if the ACPI mappings are established before the dedicated
    driver code attempts to initialize the device.  E.g. if acpi_init()
    runs before the corresponding device driver is probed, ACPI's WB mapping
    will "win", and result in the driver's ioremap() failing because the
    existing WB mapping isn't compatible with the requested WC/UC-.
    
    E.g. when a TPM is emulated by the hypervisor (ignoring the security
    implications of relying on what is allegedly an untrusted entity to store
    measurements), the TPM driver will request UC and fail:
    
      [  1.730459] ioremap error for 0xfed40000-0xfed45000, requested 0x2, got 0x0
      [  1.732780] tpm_tis MSFT0101:00: probe with driver tpm_tis failed with error -12
    
    Note, the '0x2' and '0x0' values refer to "enum page_cache_mode", not x86's
    memtypes (which frustratingly are an almost pure inversion; 2 == WB, 0 == UC).
    E.g. tracing mapping requests for TPM TIS yields:
    
     Mapping TPM TIS with req_type = 0
     WARNING: CPU: 22 PID: 1 at arch/x86/mm/pat/memtype.c:530 memtype_reserve+0x2ab/0x460
     Modules linked in:
     CPU: 22 UID: 0 PID: 1 Comm: swapper/0 Tainted: G        W           6.16.0-rc7+ #2 VOLUNTARY
     Tainted: [W]=WARN
     Hardware name: Google Google Compute Engine/Google Compute Engine, BIOS Google 05/29/2025
     RIP: 0010:memtype_reserve+0x2ab/0x460
      __ioremap_caller+0x16d/0x3d0
      ioremap_cache+0x17/0x30
      x86_acpi_os_ioremap+0xe/0x20
      acpi_os_map_iomem+0x1f3/0x240
      acpi_os_map_memory+0xe/0x20
      acpi_ex_system_memory_space_handler+0x273/0x440
      acpi_ev_address_space_dispatch+0x176/0x4c0
      acpi_ex_access_region+0x2ad/0x530
      acpi_ex_field_datum_io+0xa2/0x4f0
      acpi_ex_extract_from_field+0x296/0x3e0
      acpi_ex_read_data_from_field+0xd1/0x460
      acpi_ex_resolve_node_to_value+0x2ee/0x530
      acpi_ex_resolve_to_value+0x1f2/0x540
      acpi_ds_evaluate_name_path+0x11b/0x190
      acpi_ds_exec_end_op+0x456/0x960
      acpi_ps_parse_loop+0x27a/0xa50
      acpi_ps_parse_aml+0x226/0x600
      acpi_ps_execute_method+0x172/0x3e0
      acpi_ns_evaluate+0x175/0x5f0
      acpi_evaluate_object+0x213/0x490
      acpi_evaluate_integer+0x6d/0x140
      acpi_bus_get_status+0x93/0x150
      acpi_add_single_object+0x43a/0x7c0
      acpi_bus_check_add+0x149/0x3a0
      acpi_bus_check_add_1+0x16/0x30
      acpi_ns_walk_namespace+0x22c/0x360
      acpi_walk_namespace+0x15c/0x170
      acpi_bus_scan+0x1dd/0x200
      acpi_scan_init+0xe5/0x2b0
      acpi_init+0x264/0x5b0
      do_one_initcall+0x5a/0x310
      kernel_init_freeable+0x34f/0x4f0
      kernel_init+0x1b/0x200
      ret_from_fork+0x186/0x1b0
      ret_from_fork_asm+0x1a/0x30
      </TASK>
    
    The above traces are from a Google-VMM based VM, but the same behavior
    happens with a QEMU based VM that is modified to add a SystemMemory range
    for the TPM TIS address space.
    
    The only reason this doesn't cause problems for HPET, which appears to
    require a SystemMemory region, is because HPET gets special treatment via
    x86_init.timers.timer_init(), and so gets a chance to create its UC-
    mapping before acpi_init() clobbers things.  Disabling the early call to
    hpet_time_init() yields the same behavior for HPET:
    
      [  0.318264] ioremap error for 0xfed00000-0xfed01000, requested 0x2, got 0x0
    
    Hack around the ACPI gap by forcing the legacy PCI hole to UC when
    overriding the (virtual) MTRRs for CoCo guest, so that ioremap handling
    of MTRRs naturally kicks in and forces the ACPI mappings to be UC.
    
    Note, the requested/mapped memtype doesn't actually matter in terms of
    accessing the device.  In practically every setup, legacy PCI devices are
    emulated by the hypervisor, and accesses are intercepted and handled as
    emulated MMIO, i.e. never access physical memory and thus don't have an
    effective memtype.
    
    Even in a theoretical setup where such devices are passed through by the
    host, i.e. point at real MMIO memory, it is KVM's (as the hypervisor)
    responsibility to force the memory to be WC/UC, e.g. via EPT memtype
    under TDX or real hardware MTRRs under SNP.  Not doing so cannot work,
    and the hypervisor is highly motivated to do the right thing as letting
    the guest access hardware MMIO with WB would likely result in a variety
    of fatal #MCs.
    
    In other words, forcing the range to be UC is all about coercing the
    kernel's tracking into thinking that it has established UC mappings, so
    that the ioremap code doesn't reject mappings from e.g. the TPM driver and
    thus prevent the driver from loading and the device from functioning.
    
    Note #2, relying on guest firmware to handle this scenario, e.g. by setting
    virtual MTRRs and then consuming them in Linux, is not a viable option, as
    the virtual MTRR state is managed by the untrusted hypervisor, and because
    OVMF at least has stopped programming virtual MTRRs when running as a TDX
    guest.
    
    Link: https://lore.kernel.org/all/8137d98e-8825-415b-9282-1d2a115bb51a@linux.intel.com
    Fixes: 8e690b817e38 ("x86/kvm: Override default caching mode for SEV-SNP and TDX")
    Cc: stable@vger.kernel.org
    Cc: Peter Gonda <pgonda@google.com>
    Cc: Vitaly Kuznetsov <vkuznets@redhat.com>
    Cc: Tom Lendacky <thomas.lendacky@amd.com>
    Cc: Jürgen Groß <jgross@suse.com>
    Cc: Korakit Seemakhupt <korakit@google.com>
    Cc: Jianxiong Gao <jxgao@google.com>
    Cc: Nikolay Borisov <nik.borisov@suse.com>
    Suggested-by: Binbin Wu <binbin.wu@linux.intel.com>
    Reviewed-by: Binbin Wu <binbin.wu@linux.intel.com>
    Tested-by: Korakit Seemakhupt <korakit@google.com>
    Link: https://lore.kernel.org/r/20250828005249.39339-1-seanjc@google.com
    Signed-off-by: Sean Christopherson <seanjc@google.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 05ec0186b4ab102eca5dc90d22d16b7f186ff384
Author: Fuad Tabba <tabba@google.com>
Date:   Wed Sep 17 14:07:37 2025 +0100

    KVM: arm64: Fix page leak in user_mem_abort()
    
    commit 5f9466b50c1b4253d91abf81780b90a722133162 upstream.
    
    The user_mem_abort() function acquires a page reference via
    __kvm_faultin_pfn() early in its execution. However, the subsequent
    checks for mismatched attributes between stage 1 and stage 2 mappings
    would return an error code directly, bypassing the corresponding page
    release.
    
    Fix this by storing the error and releasing the unused page before
    returning the error.
    
    Fixes: 6d674e28f642 ("KVM: arm/arm64: Properly handle faulting of device mappings")
    Fixes: 2a8dfab26677 ("KVM: arm64: Block cacheable PFNMAP mapping")
    Signed-off-by: Fuad Tabba <tabba@google.com>
    Reviewed-by: Oliver Upton <oliver.upton@linux.dev>
    Signed-off-by: Marc Zyngier <maz@kernel.org>
    Cc: stable@vger.kernel.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 4f7af3d8a1177c807d1f2563c7c171700b020656
Author: Ben Horgan <ben.horgan@arm.com>
Date:   Fri Aug 15 17:26:55 2025 +0100

    KVM: arm64: Fix debug checking for np-guests using huge mappings
    
    commit 2ba972bf71cb71d2127ec6c3db1ceb6dd0c73173 upstream.
    
    When running with transparent huge pages and CONFIG_NVHE_EL2_DEBUG then
    the debug checking in assert_host_shared_guest() fails on the launch of an
    np-guest. This WARN_ON() causes a panic and generates the stack below.
    
    In __pkvm_host_relax_perms_guest() the debug checking assumes the mapping
    is a single page but it may be a block map. Update the checking so that
    the size is not checked and just assumes the correct size.
    
    While we're here make the same fix in __pkvm_host_mkyoung_guest().
    
      Info: # lkvm run -k /share/arch/arm64/boot/Image -m 704 -c 8 --name guest-128
      Info: Removed ghost socket file "/.lkvm//guest-128.sock".
    [ 1406.521757] kvm [141]: nVHE hyp BUG at: arch/arm64/kvm/hyp/nvhe/mem_protect.c:1088!
    [ 1406.521804] kvm [141]: nVHE call trace:
    [ 1406.521828] kvm [141]:  [<ffff8000811676b4>] __kvm_nvhe_hyp_panic+0xb4/0xe8
    [ 1406.521946] kvm [141]:  [<ffff80008116d12c>] __kvm_nvhe_assert_host_shared_guest+0xb0/0x10c
    [ 1406.522049] kvm [141]:  [<ffff80008116f068>] __kvm_nvhe___pkvm_host_relax_perms_guest+0x48/0x104
    [ 1406.522157] kvm [141]:  [<ffff800081169df8>] __kvm_nvhe_handle___pkvm_host_relax_perms_guest+0x64/0x7c
    [ 1406.522250] kvm [141]:  [<ffff800081169f0c>] __kvm_nvhe_handle_trap+0x8c/0x1a8
    [ 1406.522333] kvm [141]:  [<ffff8000811680fc>] __kvm_nvhe___skip_pauth_save+0x4/0x4
    [ 1406.522454] kvm [141]: ---[ end nVHE call trace ]---
    [ 1406.522477] kvm [141]: Hyp Offset: 0xfffece8013600000
    [ 1406.522554] Kernel panic - not syncing: HYP panic:
    [ 1406.522554] PS:834003c9 PC:0000b1806db6d170 ESR:00000000f2000800
    [ 1406.522554] FAR:ffff8000804be420 HPFAR:0000000000804be0 PAR:0000000000000000
    [ 1406.522554] VCPU:0000000000000000
    [ 1406.523337] CPU: 3 UID: 0 PID: 141 Comm: kvm-vcpu-0 Not tainted 6.16.0-rc7 #97 PREEMPT
    [ 1406.523485] Hardware name: FVP Base RevC (DT)
    [ 1406.523566] Call trace:
    [ 1406.523629]  show_stack+0x18/0x24 (C)
    [ 1406.523753]  dump_stack_lvl+0xd4/0x108
    [ 1406.523899]  dump_stack+0x18/0x24
    [ 1406.524040]  panic+0x3d8/0x448
    [ 1406.524184]  nvhe_hyp_panic_handler+0x10c/0x23c
    [ 1406.524325]  kvm_handle_guest_abort+0x68c/0x109c
    [ 1406.524500]  handle_exit+0x60/0x17c
    [ 1406.524630]  kvm_arch_vcpu_ioctl_run+0x2e0/0x8c0
    [ 1406.524794]  kvm_vcpu_ioctl+0x1a8/0x9cc
    [ 1406.524919]  __arm64_sys_ioctl+0xac/0x104
    [ 1406.525067]  invoke_syscall+0x48/0x10c
    [ 1406.525189]  el0_svc_common.constprop.0+0x40/0xe0
    [ 1406.525322]  do_el0_svc+0x1c/0x28
    [ 1406.525441]  el0_svc+0x38/0x120
    [ 1406.525588]  el0t_64_sync_handler+0x10c/0x138
    [ 1406.525750]  el0t_64_sync+0x1ac/0x1b0
    [ 1406.525876] SMP: stopping secondary CPUs
    [ 1406.525965] Kernel Offset: disabled
    [ 1406.526032] CPU features: 0x0000,00000080,8e134ca1,9446773f
    [ 1406.526130] Memory Limit: none
    [ 1406.959099] ---[ end Kernel panic - not syncing: HYP panic:
    [ 1406.959099] PS:834003c9 PC:0000b1806db6d170 ESR:00000000f2000800
    [ 1406.959099] FAR:ffff8000804be420 HPFAR:0000000000804be0 PAR:0000000000000000
    [ 1406.959099] VCPU:0000000000000000 ]
    
    Signed-off-by: Ben Horgan <ben.horgan@arm.com>
    Fixes: f28f1d02f4eaa ("KVM: arm64: Add a range to __pkvm_host_unshare_guest()")
    Cc: Vincent Donnefort <vdonnefort@google.com>
    Cc: Quentin Perret <qperret@google.com>
    Cc: Ryan Roberts <ryan.roberts@arm.com>
    Cc: stable@vger.kernel.org
    Reviewed-by: Vincent Donnefort <vdonnefort@google.com>
    Signed-off-by: Marc Zyngier <maz@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 919efcadb63fc3d3a82c3de7194140e0b28903dc
Author: Gautam Gala <ggala@linux.ibm.com>
Date:   Wed Sep 24 13:26:44 2025 +0200

    KVM: s390: Fix to clear PTE when discarding a swapped page
    
    commit 5deafa27d9ae040b75d392f60b12e300b42b4792 upstream.
    
    KVM run fails when guests with 'cmm' cpu feature and host are
    under memory pressure and use swap heavily. This is because
    npages becomes ENOMEN (out of memory) in hva_to_pfn_slow()
    which inturn propagates as EFAULT to qemu. Clearing the page
    table entry when discarding an address that maps to a swap
    entry resolves the issue.
    
    Fixes: 200197908dc4 ("KVM: s390: Refactor and split some gmap helpers")
    Cc: stable@vger.kernel.org
    Suggested-by: Claudio Imbrenda <imbrenda@linux.ibm.com>
    Signed-off-by: Gautam Gala <ggala@linux.ibm.com>
    Reviewed-by: Claudio Imbrenda <imbrenda@linux.ibm.com>
    Signed-off-by: Claudio Imbrenda <imbrenda@linux.ibm.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 3d0dc6c9f903beaf74c0d0b7dd3e38674263a3c2
Author: Robin Murphy <robin.murphy@arm.com>
Date:   Thu Sep 18 17:25:31 2025 +0100

    perf/arm-cmn: Fix CMN S3 DTM offset
    
    commit b3fe1c83a56f3cb7c475747ee1c6ec5a9dd5f60e upstream.
    
    CMN S3's DTM offset is different between r0px and r1p0, and it
    turns out this was not a error in the earlier documentation, but
    does actually exist in the design. Lovely.
    
    Cc: stable@vger.kernel.org
    Fixes: 0dc2f4963f7e ("perf/arm-cmn: Support CMN S3")
    Signed-off-by: Robin Murphy <robin.murphy@arm.com>
    Signed-off-by: Will Deacon <will@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a51bf5996473ebbd14f34dee33037e7f112e1ca2
Author: Johan Hovold <johan@kernel.org>
Date:   Fri Aug 29 15:21:52 2025 +0200

    firmware: arm_scmi: quirk: Prevent writes to string constants
    
    commit 572ce546390d1b7c99b16c38cae1b680c716216c upstream.
    
    The quirk version range is typically a string constant and must not be
    modified (e.g. as it may be stored in read-only memory). Attempting
    to do so can trigger faults such as:
    
      |  Unable to handle kernel write to read-only memory at virtual
      |  address ffffc036d998a947
    
    Update the range parsing so that it operates on a copy of the version
    range string, and mark all the quirk strings as const to reduce the
    risk of introducing similar future issues.
    
    Closes: https://bugzilla.kernel.org/show_bug.cgi?id=220437
    Fixes: 487c407d57d6 ("firmware: arm_scmi: Add common framework to handle firmware quirks")
    Cc: stable@vger.kernel.org      # 6.16
    Cc: Cristian Marussi <cristian.marussi@arm.com>
    Reported-by: Jan Palus <jpalus@fastmail.com>
    Signed-off-by: Johan Hovold <johan@kernel.org>
    Message-Id: <20250829132152.28218-1-johan@kernel.org>
    [sudeep.holla: minor commit message rewording; switch to cleanup helpers]
    Signed-off-by: Sudeep Holla <sudeep.holla@arm.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a1202b7922d547078d56dee1adbaa9095e7ce94e
Author: Miaoqian Lin <linmq006@gmail.com>
Date:   Tue Sep 2 15:59:43 2025 +0800

    ARM: OMAP2+: pm33xx-core: ix device node reference leaks in amx3_idle_init
    
    commit 74139a64e8cedb6d971c78d5d17384efeced1725 upstream.
    
    Add missing of_node_put() calls to release
    device node references obtained via of_parse_phandle().
    
    Fixes: 06ee7a950b6a ("ARM: OMAP2+: pm33xx-core: Add cpuidle_ops for am335x/am437x")
    Cc: stable@vger.kernel.org
    Signed-off-by: Miaoqian Lin <linmq006@gmail.com>
    Link: https://lore.kernel.org/r/20250902075943.2408832-1-linmq006@gmail.com
    Signed-off-by: Kevin Hilman <khilman@baylibre.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit e9d7803681473d5d1aeab4b961d764e2a62676e1
Author: Alexander Sverdlin <alexander.sverdlin@gmail.com>
Date:   Thu Jul 17 17:27:03 2025 +0200

    ARM: AM33xx: Implement TI advisory 1.0.36 (EMU0/EMU1 pins state on reset)
    
    commit 8a6506e1ba0d2b831729808d958aae77604f12f9 upstream.
    
    There is an issue possible where TI AM33xx SoCs do not boot properly after
    a reset if EMU0/EMU1 pins were used as GPIO and have been driving low level
    actively prior to reset [1].
    
    "Advisory 1.0.36 EMU0 and EMU1: Terminals Must be Pulled High Before
    ICEPick Samples
    
    The state of the EMU[1:0] terminals are latched during reset to determine
    ICEPick boot mode. For normal device operation, these terminals must be
    pulled up to a valid high logic level ( > VIH min) before ICEPick samples
    the state of these terminals, which occurs
    [five CLK_M_OSC clock cycles - 10 ns] after the falling edge of WARMRSTn.
    
    Many applications may not require the secondary GPIO function of the
    EMU[1:0] terminals. In this case, they would only be connected to pull-up
    resistors, which ensures they are always high when ICEPick samples.
    However, some applications may need to use these terminals as GPIO where
    they could be driven low before reset is asserted. This usage of the
    EMU[1:0] terminals may require special attention to ensure the terminals
    are allowed to return to a valid high-logic level before ICEPick samples
    the state of these terminals.
    
    When any device reset is asserted, the pin mux mode of EMU[1:0] terminals
    configured to operate as GPIO (mode 7) will change back to EMU input
    (mode 0) on the falling edge of WARMRSTn. This only provides a short period
    of time for the terminals to return high if driven low before reset is
    asserted...
    
    If the EMU[1:0] terminals are configured to operate as GPIO, the product
    should be designed such these terminals can be pulled to a valid high-logic
    level within 190 ns after the falling edge of WARMRSTn."
    
    We've noticed this problem with custom am335x hardware in combination with
    recently implemented cold reset method
    (commit 6521f6a195c70 ("ARM: AM33xx: PRM: Implement REBOOT_COLD")).
    It looks like the problem can affect other HW, for instance AM335x
    Chiliboard, because the latter has LEDs on GPIO3_7/GPIO3_8 as well.
    
    One option would be to check if the pins are in GPIO mode and either switch
    to output active high, or switch to input and poll until the external
    pull-ups have brought the pins to the desired high state. But fighting
    with GPIO driver for these pins is probably not the most straight forward
    approch in a reboot handler.
    
    Fortunately we can easily control pinmuxing here and rely on the external
    pull-ups. TI recommends 4k7 external pull up resistors [2] and even with
    quite conservative estimation for pin capacity (1 uF should never happen)
    the required delay shall not exceed 5ms.
    
    [1] Link: https://www.ti.com/lit/pdf/sprz360
    [2] Link: https://e2e.ti.com/support/processors-group/processors/f/processors-forum/866346/am3352-emu-1-0-questions
    
    Cc: stable@vger.kernel.org
    Signed-off-by: Alexander Sverdlin <alexander.sverdlin@siemens.com>
    Link: https://lore.kernel.org/r/20250717152708.487891-1-alexander.sverdlin@siemens.com
    Signed-off-by: Kevin Hilman <khilman@baylibre.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 8354feca6bab70679ed207a323bff4605074f15e
Author: Catalin Marinas <catalin.marinas@arm.com>
Date:   Wed Sep 24 13:31:22 2025 +0100

    arm64: mte: Do not flag the zero page as PG_mte_tagged
    
    commit f620d66af3165838bfa845dcf9f5f9b4089bf508 upstream.
    
    Commit 68d54ceeec0e ("arm64: mte: Allow PTRACE_PEEKMTETAGS access to the
    zero page") attempted to fix ptrace() reading of tags from the zero page
    by marking it as PG_mte_tagged during cpu_enable_mte(). The same commit
    also changed the ptrace() tag access permission check to the VM_MTE vma
    flag while turning the page flag test into a WARN_ON_ONCE().
    
    Attempting to set the PG_mte_tagged flag early with
    CONFIG_DEFERRED_STRUCT_PAGE_INIT enabled may either hang (after commit
    d77e59a8fccd "arm64: mte: Lock a page for MTE tag initialisation") or
    have the flags cleared later during page_alloc_init_late(). In addition,
    pages_identical() -> memcmp_pages() will reject any comparison with the
    zero page as it is marked as tagged.
    
    Partially revert the above commit to avoid setting PG_mte_tagged on the
    zero page. Update the __access_remote_tags() warning on untagged pages
    to ignore the zero page since it is known to have the tags initialised.
    
    Note that all user mapping of the zero page are marked as pte_special().
    The arm64 set_pte_at() will not call mte_sync_tags() on such pages, so
    PG_mte_tagged will remain cleared.
    
    Signed-off-by: Catalin Marinas <catalin.marinas@arm.com>
    Fixes: 68d54ceeec0e ("arm64: mte: Allow PTRACE_PEEKMTETAGS access to the zero page")
    Reported-by: Gergely Kovacs <Gergely.Kovacs2@arm.com>
    Cc: stable@vger.kernel.org # 5.10.x
    Cc: Will Deacon <will@kernel.org>
    Cc: David Hildenbrand <david@redhat.com>
    Cc: Lance Yang <lance.yang@linux.dev>
    Acked-by: Lance Yang <lance.yang@linux.dev>
    Reviewed-by: David Hildenbrand <david@redhat.com>
    Tested-by: Lance Yang <lance.yang@linux.dev>
    Signed-off-by: Will Deacon <will@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit e5137ed13936caa6d9d64063b1523b1b2dcf0eb0
Author: Yang Shi <yang@os.amperecomputing.com>
Date:   Thu Sep 18 09:23:49 2025 -0700

    arm64: kprobes: call set_memory_rox() for kprobe page
    
    commit 195a1b7d8388c0ec2969a39324feb8bebf9bb907 upstream.
    
    The kprobe page is allocated by execmem allocator with ROX permission.
    It needs to call set_memory_rox() to set proper permission for the
    direct map too. It was missed.
    
    Fixes: 10d5e97c1bf8 ("arm64: use PAGE_KERNEL_ROX directly in alloc_insn_page")
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Yang Shi <yang@os.amperecomputing.com>
    Reviewed-by: Catalin Marinas <catalin.marinas@arm.com>
    Signed-off-by: Will Deacon <will@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 1d37ec09c9fc60ad47a95a0b53d9fbd77afb47ac
Author: Judith Mendez <jm@ti.com>
Date:   Mon Aug 18 14:26:32 2025 -0500

    arm64: dts: ti: k3-am62p: Fix supported hardware for 1GHz OPP
    
    commit f434ec2200667d5362bd19f93a498d9b3f121588 upstream.
    
    The 1GHz OPP is supported on speed grade "O" as well according to the
    device datasheet [0], so fix the opp-supported-hw property to support
    this speed grade for 1GHz OPP.
    
    [0] https://www.ti.com/lit/gpn/am62p
    Fixes: 76d855f05801 ("arm64: dts: ti: k3-am62p: add opp frequencies")
    Cc: stable@vger.kernel.org
    Signed-off-by: Judith Mendez <jm@ti.com>
    Signed-off-by: Viresh Kumar <viresh.kumar@linaro.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit ef0429fba4670f7f5e63d60c214bb231d0b7d7cc
Author: Vibhore Vardhan <vibhore@ti.com>
Date:   Wed Sep 3 11:55:12 2025 +0530

    arm64: dts: ti: k3-am62a-main: Fix main padcfg length
    
    commit 4c4e48afb6d85c1a8f9fdbae1fdf17ceef4a6f5b upstream.
    
    The main pad configuration register region starts with the register
    MAIN_PADCFG_CTRL_MMR_CFG0_PADCONFIG0 with address 0x000f4000 and ends
    with the MAIN_PADCFG_CTRL_MMR_CFG0_PADCONFIG150 register with address
    0x000f4258, as a result of which, total size of the region is 0x25c
    instead of 0x2ac.
    
    Reference Docs
    TRM (AM62A) - https://www.ti.com/lit/ug/spruj16b/spruj16b.pdf
    TRM (AM62D) - https://www.ti.com/lit/ug/sprujd4/sprujd4.pdf
    
    Fixes: 5fc6b1b62639c ("arm64: dts: ti: Introduce AM62A7 family of SoCs")
    Cc: stable@vger.kernel.org
    Signed-off-by: Vibhore Vardhan <vibhore@ti.com>
    Signed-off-by: Paresh Bhagat <p-bhagat@ti.com>
    Reviewed-by: Siddharth Vadapalli <s-vadapalli@ti.com>
    Link: https://patch.msgid.link/20250903062513.813925-2-p-bhagat@ti.com
    Signed-off-by: Nishanth Menon <nm@ti.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 33d5cc52ca3ba29c255936512cbc13fa98346c17
Author: Aleksandrs Vinarskis <alex.vinarskis@gmail.com>
Date:   Tue Jul 1 20:35:53 2025 +0200

    arm64: dts: qcom: x1e80100-pmics: Disable pm8010 by default
    
    commit b9a185198f96259311543b30d884d8c01da913f7 upstream.
    
    pm8010 is a camera specific PMIC, and may not be present on some
    devices. These may instead use a dedicated vreg for this purpose (Dell
    XPS 9345, Dell Inspiron..) or use USB webcam instead of a MIPI one
    alltogether (Lenovo Thinbook 16, Lenovo Yoga..).
    
    Disable pm8010 by default, let platforms that actually have one onboard
    enable it instead.
    
    Cc: stable@vger.kernel.org
    Fixes: 2559e61e7ef4 ("arm64: dts: qcom: x1e80100-pmics: Add the missing PMICs")
    Reviewed-by: Bryan O'Donoghue <bryan.odonoghue@linaro.org>
    Reviewed-by: Johan Hovold <johan+linaro@kernel.org>
    Reviewed-by: Konrad Dybcio <konrad.dybcio@oss.qualcomm.com>
    Signed-off-by: Aleksandrs Vinarskis <alex.vinarskis@gmail.com>
    Link: https://lore.kernel.org/r/20250701183625.1968246-2-alex.vinarskis@gmail.com
    Signed-off-by: Bjorn Andersson <andersson@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit ed4e3ce6dd3d23530216fa697907b3d307cd2950
Author: Stephan Gerhold <stephan.gerhold@linaro.org>
Date:   Thu Aug 21 10:15:09 2025 +0200

    arm64: dts: qcom: sdm845: Fix slimbam num-channels/ees
    
    commit 316294bb6695a43a9181973ecd4e6fb3e576a9f7 upstream.
    
    Reading the hardware registers of the &slimbam on RB3 reveals that the BAM
    supports only 23 pipes (channels) and supports 4 EEs instead of 2. This
    hasn't caused problems so far since nothing is using the extra channels,
    but attempting to use them would lead to crashes.
    
    The bam_dma driver might warn in the future if the num-channels in the DT
    are wrong, so correct the properties in the DT to avoid future regressions.
    
    Cc: stable@vger.kernel.org
    Fixes: 27ca1de07dc3 ("arm64: dts: qcom: sdm845: add slimbus nodes")
    Signed-off-by: Stephan Gerhold <stephan.gerhold@linaro.org>
    Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@oss.qualcomm.com>
    Link: https://lore.kernel.org/r/20250821-sdm845-slimbam-channels-v1-1-498f7d46b9ee@linaro.org
    Signed-off-by: Bjorn Andersson <andersson@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f00e9ea8987f7350d6312fc749ca1ea1a3bfbe43
Author: Stephan Gerhold <stephan.gerhold@linaro.org>
Date:   Mon Sep 15 15:28:31 2025 +0200

    arm64: dts: qcom: msm8939: Add missing MDSS reset
    
    commit f73c82c855e186e9b67125e3eee743960320e43c upstream.
    
    On most MSM8939 devices, the bootloader already initializes the display to
    show the boot splash screen. In this situation, MDSS is already configured
    and left running when starting Linux. To avoid side effects from the
    bootloader configuration, the MDSS reset can be specified in the device
    tree to start again with a clean hardware state.
    
    The reset for MDSS is currently missing in msm8939.dtsi, which causes
    errors when the MDSS driver tries to re-initialize the registers:
    
     dsi_err_worker: status=6
     dsi_err_worker: status=6
     dsi_err_worker: status=6
     ...
    
    It turns out that we have always indirectly worked around this by building
    the MDSS driver as a module. Before v6.17, the power domain was temporarily
    turned off until the module was loaded, long enough to clear the register
    contents. In v6.17, power domains are not turned off during boot until
    sync_state() happens, so this is no longer working. Even before v6.17 this
    resulted in broken behavior, but notably only when the MDSS driver was
    built-in instead of a module.
    
    Cc: stable@vger.kernel.org
    Fixes: 61550c6c156c ("arm64: dts: qcom: Add msm8939 SoC")
    Signed-off-by: Stephan Gerhold <stephan.gerhold@linaro.org>
    Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@oss.qualcomm.com>
    Reviewed-by: Konrad Dybcio <konrad.dybcio@oss.qualcomm.com>
    Link: https://lore.kernel.org/r/20250915-msm8916-resets-v1-2-a5c705df0c45@linaro.org
    Signed-off-by: Bjorn Andersson <andersson@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a42f35fb3e4ba3aab5e8504980c4cff2ac94571b
Author: Stephan Gerhold <stephan.gerhold@linaro.org>
Date:   Mon Sep 15 15:28:30 2025 +0200

    arm64: dts: qcom: msm8916: Add missing MDSS reset
    
    commit 99b78773c2ae55dcc01025f94eae8ce9700ae985 upstream.
    
    On most MSM8916 devices (aside from the DragonBoard 410c), the bootloader
    already initializes the display to show the boot splash screen. In this
    situation, MDSS is already configured and left running when starting Linux.
    To avoid side effects from the bootloader configuration, the MDSS reset can
    be specified in the device tree to start again with a clean hardware state.
    
    The reset for MDSS is currently missing in msm8916.dtsi, which causes
    errors when the MDSS driver tries to re-initialize the registers:
    
     dsi_err_worker: status=6
     dsi_err_worker: status=6
     dsi_err_worker: status=6
     ...
    
    It turns out that we have always indirectly worked around this by building
    the MDSS driver as a module. Before v6.17, the power domain was temporarily
    turned off until the module was loaded, long enough to clear the register
    contents. In v6.17, power domains are not turned off during boot until
    sync_state() happens, so this is no longer working. Even before v6.17 this
    resulted in broken behavior, but notably only when the MDSS driver was
    built-in instead of a module.
    
    Cc: stable@vger.kernel.org
    Fixes: 305410ffd1b2 ("arm64: dts: msm8916: Add display support")
    Signed-off-by: Stephan Gerhold <stephan.gerhold@linaro.org>
    Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@oss.qualcomm.com>
    Reviewed-by: Konrad Dybcio <konrad.dybcio@oss.qualcomm.com>
    Link: https://lore.kernel.org/r/20250915-msm8916-resets-v1-1-a5c705df0c45@linaro.org
    Signed-off-by: Bjorn Andersson <andersson@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit fbf6074d19192991cb89d26f14d73017151a9d89
Author: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Date:   Sun Sep 28 12:18:29 2025 +0200

    ACPI: battery: Add synchronization between interface updates
    
    commit 399dbcadc01ebf0035f325eaa8c264f8b5cd0a14 upstream.
    
    There is no synchronization between different code paths in the ACPI
    battery driver that update its sysfs interface or its power supply
    class device interface.  In some cases this results to functional
    failures due to race conditions.
    
    One example of this is when two ACPI notifications:
    
      - ACPI_BATTERY_NOTIFY_STATUS (0x80)
      - ACPI_BATTERY_NOTIFY_INFO   (0x81)
    
    are triggered (by the platform firmware) in a row with a little delay
    in between after removing and reinserting a laptop battery.  Both
    notifications cause acpi_battery_update() to be called and if the delay
    between them is sufficiently small, sysfs_add_battery() can be re-entered
    before battery->bat is set which leads to a duplicate sysfs entry error:
    
     sysfs: cannot create duplicate filename '/devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0A:00/power_supply/BAT1'
     CPU: 1 UID: 0 PID: 185 Comm: kworker/1:4 Kdump: loaded Not tainted 6.12.38+deb13-amd64 #1  Debian 6.12.38-1
     Hardware name: Gateway          NV44             /SJV40-MV        , BIOS V1.3121 04/08/2009
     Workqueue: kacpi_notify acpi_os_execute_deferred
     Call Trace:
      <TASK>
      dump_stack_lvl+0x5d/0x80
      sysfs_warn_dup.cold+0x17/0x23
      sysfs_create_dir_ns+0xce/0xe0
      kobject_add_internal+0xba/0x250
      kobject_add+0x96/0xc0
      ? get_device_parent+0xde/0x1e0
      device_add+0xe2/0x870
      __power_supply_register.part.0+0x20f/0x3f0
      ? wake_up_q+0x4e/0x90
      sysfs_add_battery+0xa4/0x1d0 [battery]
      acpi_battery_update+0x19e/0x290 [battery]
      acpi_battery_notify+0x50/0x120 [battery]
      acpi_ev_notify_dispatch+0x49/0x70
      acpi_os_execute_deferred+0x1a/0x30
      process_one_work+0x177/0x330
      worker_thread+0x251/0x390
      ? __pfx_worker_thread+0x10/0x10
      kthread+0xd2/0x100
      ? __pfx_kthread+0x10/0x10
      ret_from_fork+0x34/0x50
      ? __pfx_kthread+0x10/0x10
      ret_from_fork_asm+0x1a/0x30
      </TASK>
     kobject: kobject_add_internal failed for BAT1 with -EEXIST, don't try to register things with the same name in the same directory.
    
    There are also other scenarios in which analogous issues may occur.
    
    Address this by using a common lock in all of the code paths leading
    to updates of driver interfaces: ACPI Notify () handler, system resume
    callback and post-resume notification, device addition and removal.
    
    This new lock replaces sysfs_lock that has been used only in
    sysfs_remove_battery() which now is going to be always called under
    the new lock, so it doesn't need any internal locking any more.
    
    Fixes: 10666251554c ("ACPI: battery: Install Notify() handler directly")
    Closes: https://lore.kernel.org/linux-acpi/20250910142653.313360-1-luogf2025@163.com/
    Reported-by: GuangFei Luo <luogf2025@163.com>
    Tested-by: GuangFei Luo <luogf2025@163.com>
    Cc: 6.6+ <stable@vger.kernel.org> # 6.6+
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 70aa2ff980e339bb50720b203304fb1d0c5b5f82
Author: Amir Mohammad Jahangirzad <a.jahangirzad@gmail.com>
Date:   Tue Sep 23 05:01:13 2025 +0330

    ACPI: debug: fix signedness issues in read/write helpers
    
    commit 496f9372eae14775e0524e83e952814691fe850a upstream.
    
    In the ACPI debugger interface, the helper functions for read and write
    operations use "int" as the length parameter data type. When a large
    "size_t count" is passed from the file operations, this cast to "int"
    results in truncation and a negative value due to signed integer
    representation.
    
    Logically, this negative number propagates to the min() calculation,
    where it is selected over the positive buffer space value, leading to
    unexpected behavior. Subsequently, when this negative value is used in
    copy_to_user() or copy_from_user(), it is interpreted as a large positive
    value due to the unsigned nature of the size parameter in these functions,
    causing the copy operations to attempt handling sizes far beyond the
    intended buffer limits.
    
    Address the issue by:
     - Changing the length parameters in acpi_aml_read_user() and
       acpi_aml_write_user() from "int" to "size_t", aligning with the
       expected unsigned size semantics.
     - Updating return types and local variables in acpi_aml_read() and
       acpi_aml_write() to "ssize_t" for consistency with kernel file
       operation conventions.
     - Using "size_t" for the "n" variable to ensure calculations remain
       unsigned.
     - Using min_t() for circ_count_to_end() and circ_space_to_end() to
       ensure type-safe comparisons and prevent integer overflow.
    
    Signed-off-by: Amir Mohammad Jahangirzad <a.jahangirzad@gmail.com>
    Link: https://patch.msgid.link/20250923013113.20615-1-a.jahangirzad@gmail.com
    [ rjw: Changelog tweaks, local variable definitions ordering adjustments ]
    Fixes: 8cfb0cdf07e2 ("ACPI / debugger: Add IO interface to access debugger functionalities")
    Cc: 4.5+ <stable@vger.kernel.org> # 4.5+
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit cfe0784a7432523fac0f7b75c49f2cabc3eb8eb4
Author: Ahmed Salem <x0rw3ll@gmail.com>
Date:   Fri Sep 12 21:59:17 2025 +0200

    ACPICA: Debugger: drop ACPI_NONSTRING attribute from name_seg
    
    commit 22c65572eff14a6e9546a9dbaa333619eb5505ab upstream.
    
    ACPICA commit 4623b3369f3aa1ec5229d461e91c514510a96912
    
    Partially revert commit 70662db73d54 ("ACPICA: Apply ACPI_NONSTRING in
    more places") as I've yet again incorrectly applied the ACPI_NONSTRING
    attribute where it is not needed.
    
    A warning was initially reported by Collin Funk [1], and further review
    by Jiri Slaby [2] highlighted another issue related to the same commit.
    
    Drop the ACPI_NONSTRING attribute to fix the issue.
    
    Fixes: 70662db73d54 ("ACPICA: Apply ACPI_NONSTRING in more places")
    Link: https://lore.kernel.org/all/87ecvpcypw.fsf@gmail.com [1]
    Link: https://lore.kernel.org/all/5c210121-c9b8-4458-b1ad-0da24732ac72@kernel.org [2]
    Link: https://github.com/acpica/acpica/commit/4623b336
    Reported-by: Jiri Slaby <jirislaby@kernel.org>
    Signed-off-by: Ahmed Salem <x0rw3ll@gmail.com>
    Cc: 6.16+ <stable@vger.kernel.org> # 6.16+
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 5491b74a34b5963ffd0e675abd4a01a3048104dc
Author: Daniel Tang <danielzgtg.opensource@gmail.com>
Date:   Thu Aug 28 01:38:14 2025 -0400

    ACPI: TAD: Add missing sysfs_remove_group() for ACPI_TAD_RT
    
    commit 4aac453deca0d9c61df18d968f8864c3ae7d3d8d upstream.
    
    Previously, after `rmmod acpi_tad`, `modprobe acpi_tad` would fail
    with this dmesg:
    
    sysfs: cannot create duplicate filename '/devices/platform/ACPI000E:00/time'
    Call Trace:
     <TASK>
     dump_stack_lvl+0x6c/0x90
     dump_stack+0x10/0x20
     sysfs_warn_dup+0x8b/0xa0
     sysfs_add_file_mode_ns+0x122/0x130
     internal_create_group+0x1dd/0x4c0
     sysfs_create_group+0x13/0x20
     acpi_tad_probe+0x147/0x1f0 [acpi_tad]
     platform_probe+0x42/0xb0
     </TASK>
    acpi-tad ACPI000E:00: probe with driver acpi-tad failed with error -17
    
    Fixes: 3230b2b3c1ab ("ACPI: TAD: Add low-level support for real time capability")
    Signed-off-by: Daniel Tang <danielzgtg.opensource@gmail.com>
    Reviewed-by: Mika Westerberg <mika.westerberg@linux.intel.com>
    Link: https://patch.msgid.link/2881298.hMirdbgypa@daniel-desktop3
    Cc: 5.2+ <stable@vger.kernel.org> # 5.2+
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 70f0cb2d7f9eacc810f0d7c6b34280a51af5a01a
Author: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Date:   Mon Sep 15 20:21:33 2025 +0200

    ACPI: property: Fix buffer properties extraction for subnodes
    
    commit d0759b10989c5c5aae3d455458c9fc4e8cc694f7 upstream.
    
    The ACPI handle passed to acpi_extract_properties() as the first
    argument represents the ACPI namespace scope in which to look for
    objects returning buffers associated with buffer properties.
    
    For _DSD objects located immediately under ACPI devices, this handle is
    the same as the handle of the device object holding the _DSD, but for
    data-only subnodes it is not so.
    
    First of all, data-only subnodes are represented by objects that
    cannot hold other objects in their scopes (like control methods).
    Therefore a data-only subnode handle cannot be used for completing
    relative pathname segments, so the current code in
    in acpi_nondev_subnode_extract() passing a data-only subnode handle
    to acpi_extract_properties() is invalid.
    
    Moreover, a data-only subnode of device A may be represented by an
    object located in the scope of device B (which kind of makes sense,
    for instance, if A is a B's child).  In that case, the scope in
    question would be the one of device B.  In other words, the scope
    mentioned above is the same as the scope used for subnode object
    lookup in acpi_nondev_subnode_extract().
    
    Accordingly, rearrange that function to use the same scope for the
    extraction of properties and subnode object lookup.
    
    Fixes: 103e10c69c61 ("ACPI: property: Add support for parsing buffer property UUID")
    Cc: 6.0+ <stable@vger.kernel.org> # 6.0+
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Reviewed-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Tested-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 09662fc01470585dfd45d2c10eda91e6826f67dc
Author: Ahmed Salem <x0rw3ll@gmail.com>
Date:   Fri Sep 12 21:58:25 2025 +0200

    ACPICA: acpidump: drop ACPI_NONSTRING attribute from file_name
    
    commit 16ae95800b1cc46c0d69d8d90c9c7be488421a40 upstream.
    
    Partially revert commit 70662db73d54 ("ACPICA: Apply ACPI_NONSTRING in
    more places") as I've yet again incorrectly applied the ACPI_NONSTRING
    attribute where it is not needed.
    
    A warning was initially reported by Collin Funk [1], and further review
    by Jiri Slaby [2] highlighted another issue related to the same commit.
    
    Drop the ACPI_NONSTRING attribute to fix the issue.
    
    Fixes: 70662db73d54 ("ACPICA: Apply ACPI_NONSTRING in more places")
    Link: https://lore.kernel.org/all/87ecvpcypw.fsf@gmail.com [1]
    Link: https://lore.kernel.org/all/5c210121-c9b8-4458-b1ad-0da24732ac72@kernel.org [2]
    Link: https://github.com/acpica/acpica/commit/a6ee09ca
    Reported-by: Collin Funk <collin.funk1@gmail.com>
    Signed-off-by: Ahmed Salem <x0rw3ll@gmail.com>
    Cc: 6.16+ <stable@vger.kernel.org> # 6.16+
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 3df15ad837005299a61c36f17643932b1a992641
Author: Nathan Chancellor <nathan@kernel.org>
Date:   Wed Oct 8 15:46:46 2025 -0700

    s390/vmlinux.lds.S: Move .vmlinux.info to end of allocatable sections
    
    [ Upstream commit 9338d660b79a0dfe4eb3fe9bd748054cded87d4f ]
    
    When building s390 defconfig with binutils older than 2.32, there are
    several warnings during the final linking stage:
    
      s390-linux-ld: .tmp_vmlinux1: warning: allocated section `.got.plt' not in segment
      s390-linux-ld: .tmp_vmlinux2: warning: allocated section `.got.plt' not in segment
      s390-linux-ld: vmlinux.unstripped: warning: allocated section `.got.plt' not in segment
      s390-linux-objcopy: vmlinux: warning: allocated section `.got.plt' not in segment
      s390-linux-objcopy: st7afZyb: warning: allocated section `.got.plt' not in segment
    
    binutils commit afca762f598 ("S/390: Improve partial relro support for
    64 bit") [1] in 2.32 changed where .got.plt is emitted, avoiding the
    warning.
    
    The :NONE in the .vmlinux.info output section description changes the
    segment for subsequent allocated sections. Move .vmlinux.info right
    above the discards section to place all other sections in the previously
    defined segment, .data.
    
    Fixes: 30226853d6ec ("s390: vmlinux.lds.S: explicitly handle '.got' and '.plt' sections")
    Link: https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=afca762f598d453c563f244cd3777715b1a0cb72 [1]
    Acked-by: Alexander Gordeev <agordeev@linux.ibm.com>
    Acked-by: Alexey Gladkov <legion@kernel.org>
    Acked-by: Nicolas Schier <nsc@kernel.org>
    Link: https://patch.msgid.link/20251008-kbuild-fix-modinfo-regressions-v1-3-9fc776c5887c@kernel.org
    Signed-off-by: Nathan Chancellor <nathan@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 4113ec87b3f5f37c431049c9e5c07e09e0a2edde
Author: Alexey Gladkov <legion@kernel.org>
Date:   Thu Sep 18 10:05:45 2025 +0200

    s390: vmlinux.lds.S: Reorder sections
    
    [ Upstream commit 8d18ef04f940a8d336fe7915b5ea419c3eb0c0a6 ]
    
    In the upcoming changes, the ELF_DETAILS macro will be extended with
    the ".modinfo" section, which will cause an error:
    
    >> s390x-linux-ld: .tmp_vmlinux1: warning: allocated section `.modinfo' not in segment
    >> s390x-linux-ld: .tmp_vmlinux2: warning: allocated section `.modinfo' not in segment
    >> s390x-linux-ld: vmlinux.unstripped: warning: allocated section `.modinfo' not in segment
    
    This happens because the .vmlinux.info use :NONE to override the default
    segment and tell the linker to not put the section in any segment at all.
    
    To avoid this, we need to change the sections order that will be placed
    in the default segment.
    
    Cc: Heiko Carstens <hca@linux.ibm.com>
    Cc: Vasily Gorbik <gor@linux.ibm.com>
    Cc: Alexander Gordeev <agordeev@linux.ibm.com>
    Cc: linux-s390@vger.kernel.org
    Reported-by: kernel test robot <lkp@intel.com>
    Closes: https://lore.kernel.org/oe-kbuild-all/202506062053.zbkFBEnJ-lkp@intel.com/
    Signed-off-by: Alexey Gladkov <legion@kernel.org>
    Acked-by: Heiko Carstens <hca@linux.ibm.com>
    Link: https://patch.msgid.link/20d40a7a3a053ba06a54155e777dcde7fdada1db.1758182101.git.legion@kernel.org
    Signed-off-by: Nathan Chancellor <nathan@kernel.org>
    Stable-dep-of: 9338d660b79a ("s390/vmlinux.lds.S: Move .vmlinux.info to end of allocatable sections")
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 8e5e13c8df9e6bc8f1e020f317caa6579ce6507f
Author: Nathan Chancellor <nathan@kernel.org>
Date:   Wed Oct 8 15:46:45 2025 -0700

    kbuild: Add '.rel.*' strip pattern for vmlinux
    
    [ Upstream commit 8ec3af916fe3954381cf3555ea03dc5adf4d0e8e ]
    
    Prior to binutils commit c12d9fa2afe ("Support objcopy
    --remove-section=.relaFOO") [1] in 2.32, stripping relocation sections
    required the trailing period (i.e., '.rel.*') to work properly.
    
    After commit 3e86e4d74c04 ("kbuild: keep .modinfo section in
    vmlinux.unstripped"), there is an error with binutils 2.31.1 or earlier
    because these sections are not properly removed:
    
      s390-linux-objcopy: st6tO8Ev: symbol `.modinfo' required but not present
      s390-linux-objcopy:st6tO8Ev: no symbols
    
    Add the old pattern to resolve this issue (along with a comment to allow
    cleaning this when binutils 2.32 or newer is the minimum supported
    version). While the aforementioned kbuild change exposes this, the
    pattern was originally changed by commit 71d815bf5dfd ("kbuild: Strip
    runtime const RELA sections correctly"), where it would still be
    incorrect with binutils older than 2.32.
    
    Fixes: 71d815bf5dfd ("kbuild: Strip runtime const RELA sections correctly")
    Link: https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=c12d9fa2afe7abcbe407a00e15719e1a1350c2a7 [1]
    Reported-by: Linux Kernel Functional Testing <lkft@linaro.org>
    Closes: https://lore.kernel.org/CA+G9fYvVktRhFtZXdNgVOL8j+ArsJDpvMLgCitaQvQmCx=hwOQ@mail.gmail.com/
    Acked-by: Ard Biesheuvel <ardb@kernel.org>
    Acked-by: Alexey Gladkov <legion@kernel.org>
    Acked-by: Nicolas Schier <nsc@kernel.org>
    Link: https://patch.msgid.link/20251008-kbuild-fix-modinfo-regressions-v1-2-9fc776c5887c@kernel.org
    Signed-off-by: Nathan Chancellor <nathan@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 7b80f81ae3190855c6c0d60224048a3383abab3b
Author: Nathan Chancellor <nathan@kernel.org>
Date:   Wed Oct 8 15:46:44 2025 -0700

    kbuild: Restore pattern to avoid stripping .rela.dyn from vmlinux
    
    [ Upstream commit 4b47a3aefb29c523ca66f0d28de8db15a10f9352 ]
    
    Commit 0ce5139fd96e ("kbuild: always create intermediate
    vmlinux.unstripped") removed the pattern to avoid stripping .rela.dyn
    sections added by commit e9d86b8e17e7 ("scripts: Do not strip .rela.dyn
    section"). Restore it so that .rela.dyn sections remain in the final
    vmlinux.
    
    Fixes: 0ce5139fd96e ("kbuild: always create intermediate vmlinux.unstripped")
    Acked-by: Ard Biesheuvel <ardb@kernel.org>
    Acked-by: Alexey Gladkov <legion@kernel.org>
    Acked-by: Nicolas Schier <nsc@kernel.org>
    Link: https://patch.msgid.link/20251008-kbuild-fix-modinfo-regressions-v1-1-9fc776c5887c@kernel.org
    Signed-off-by: Nathan Chancellor <nathan@kernel.org>
    Stable-dep-of: 8ec3af916fe3 ("kbuild: Add '.rel.*' strip pattern for vmlinux")
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 5b5cdb1fe434e8adc97d5037e6d05dd386c4c4c6
Author: Masahiro Yamada <masahiroy@kernel.org>
Date:   Thu Sep 18 10:05:47 2025 +0200

    kbuild: keep .modinfo section in vmlinux.unstripped
    
    [ Upstream commit 3e86e4d74c0490e5fc5a7f8de8f29e7579c9ffe5 ]
    
    Keep the .modinfo section during linking, but strip it from the final
    vmlinux.
    
    Adjust scripts/mksysmap to exclude modinfo symbols from kallsyms.
    
    This change will allow the next commit to extract the .modinfo section
    from the vmlinux.unstripped intermediate.
    
    Signed-off-by: Masahiro Yamada <masahiroy@kernel.org>
    Signed-off-by: Alexey Gladkov <legion@kernel.org>
    Reviewed-by: Nicolas Schier <nsc@kernel.org>
    Link: https://patch.msgid.link/aaf67c07447215463300fccaa758904bac42f992.1758182101.git.legion@kernel.org
    Signed-off-by: Nathan Chancellor <nathan@kernel.org>
    Stable-dep-of: 8ec3af916fe3 ("kbuild: Add '.rel.*' strip pattern for vmlinux")
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 86f364ee58420e4e0709a1134e0d0d01bcc1758b
Author: Masahiro Yamada <masahiroy@kernel.org>
Date:   Thu Sep 18 10:05:46 2025 +0200

    kbuild: always create intermediate vmlinux.unstripped
    
    [ Upstream commit 0ce5139fd96e9d415d3faaef1c575e238f9bbd67 ]
    
    Generate the intermediate vmlinux.unstripped regardless of
    CONFIG_ARCH_VMLINUX_NEEDS_RELOCS.
    
    If CONFIG_ARCH_VMLINUX_NEEDS_RELOCS is unset, vmlinux.unstripped and
    vmlinux are identiacal.
    
    This simplifies the build rule, and allows to strip more sections
    by adding them to remove-section-y.
    
    Signed-off-by: Masahiro Yamada <masahiroy@kernel.org>
    Reviewed-by: Nicolas Schier <nsc@kernel.org>
    Link: https://patch.msgid.link/a48ca543fa2305bd17324f41606dcaed9b19f2d4.1758182101.git.legion@kernel.org
    Signed-off-by: Nathan Chancellor <nathan@kernel.org>
    Stable-dep-of: 8ec3af916fe3 ("kbuild: Add '.rel.*' strip pattern for vmlinux")
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit de2d2baecc84cc7fca52eec2b9b55d89c93e3565
Author: KaFai Wan <kafai.wan@linux.dev>
Date:   Wed Oct 8 18:26:26 2025 +0800

    bpf: Avoid RCU context warning when unpinning htab with internal structs
    
    [ Upstream commit 4f375ade6aa9f37fd72d7a78682f639772089eed ]
    
    When unpinning a BPF hash table (htab or htab_lru) that contains internal
    structures (timer, workqueue, or task_work) in its values, a BUG warning
    is triggered:
     BUG: sleeping function called from invalid context at kernel/bpf/hashtab.c:244
     in_atomic(): 1, irqs_disabled(): 0, non_block: 0, pid: 14, name: ksoftirqd/0
     ...
    
    The issue arises from the interaction between BPF object unpinning and
    RCU callback mechanisms:
    1. BPF object unpinning uses ->free_inode() which schedules cleanup via
       call_rcu(), deferring the actual freeing to an RCU callback that
       executes within the RCU_SOFTIRQ context.
    2. During cleanup of hash tables containing internal structures,
       htab_map_free_internal_structs() is invoked, which includes
       cond_resched() or cond_resched_rcu() calls to yield the CPU during
       potentially long operations.
    
    However, cond_resched() or cond_resched_rcu() cannot be safely called from
    atomic RCU softirq context, leading to the BUG warning when attempting
    to reschedule.
    
    Fix this by changing from ->free_inode() to ->destroy_inode() and rename
    bpf_free_inode() to bpf_destroy_inode() for BPF objects (prog, map, link).
    This allows direct inode freeing without RCU callback scheduling,
    avoiding the invalid context warning.
    
    Reported-by: Le Chen <tom2cat@sjtu.edu.cn>
    Closes: https://lore.kernel.org/all/1444123482.1827743.1750996347470.JavaMail.zimbra@sjtu.edu.cn/
    Fixes: 68134668c17f ("bpf: Add map side support for bpf timers.")
    Suggested-by: Alexei Starovoitov <ast@kernel.org>
    Signed-off-by: KaFai Wan <kafai.wan@linux.dev>
    Acked-by: Yonghong Song <yonghong.song@linux.dev>
    Link: https://lore.kernel.org/r/20251008102628.808045-2-kafai.wan@linux.dev
    Signed-off-by: Alexei Starovoitov <ast@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 91d72b76f089206e9bac9c9505c2199cf74940b6
Author: Bartosz Golaszewski <bartosz.golaszewski@linaro.org>
Date:   Wed Sep 24 16:51:29 2025 +0200

    gpio: wcd934x: mark the GPIO controller as sleeping
    
    [ Upstream commit b5f8aa8d4bde0cf3e4595af5a536da337e5f1c78 ]
    
    The slimbus regmap passed to the GPIO driver down from MFD does not use
    fast_io. This means a mutex is used for locking and thus this GPIO chip
    must not be used in atomic context. Change the can_sleep switch in
    struct gpio_chip to true.
    
    Fixes: 59c324683400 ("gpio: wcd934x: Add support to wcd934x gpio controller")
    Signed-off-by: Bartosz Golaszewski <bartosz.golaszewski@linaro.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 01816224d74240e35087052a3160173e698f4c2c
Author: Gunnar Kudrjavets <gunnarku@amazon.com>
Date:   Thu Sep 18 18:49:40 2025 +0300

    tpm_tis: Fix incorrect arguments in tpm_tis_probe_irq_single
    
    [ Upstream commit 8a81236f2cb0882c7ea6c621ce357f7f3f601fe5 ]
    
    The tpm_tis_write8() call specifies arguments in wrong order. Should be
    (data, addr, value) not (data, value, addr). The initial correct order
    was changed during the major refactoring when the code was split.
    
    Fixes: 41a5e1cf1fe1 ("tpm/tpm_tis: Split tpm_tis driver into a core and TCG TIS compliant phy")
    Signed-off-by: Gunnar Kudrjavets <gunnarku@amazon.com>
    Reviewed-by: Justinien Bouron <jbouron@amazon.com>
    Reviewed-by: Jarkko Sakkinen <jarkko@kernel.org>
    Reviewed-by: Paul Menzel <pmenzel@molgen.mpg.de>
    Signed-off-by: Jarkko Sakkinen <jarkko@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 83d3bc866530a36a465b47cce4d2a9def2411960
Author: Pali Rohár <pali@kernel.org>
Date:   Sat Jun 7 18:11:10 2025 +0200

    cifs: Query EA $LXMOD in cifs_query_path_info() for WSL reparse points
    
    [ Upstream commit 057ac50638bcece64b3b436d3a61b70ed6c01a34 ]
    
    EA $LXMOD is required for WSL non-symlink reparse points.
    
    Fixes: ef86ab131d91 ("cifs: Fix querying of WSL CHR and BLK reparse points over SMB1")
    Signed-off-by: Pali Rohár <pali@kernel.org>
    Signed-off-by: Steve French <stfrench@microsoft.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 51011a9e3bd572f0450bca9913edc810c0b0c928
Author: Esben Haabendal <esben@geanix.com>
Date:   Fri May 16 09:23:36 2025 +0200

    rtc: isl12022: Fix initial enable_irq/disable_irq balance
    
    [ Upstream commit 9ffe06b6ccd7a8eaa31d31625db009ea26a22a3c ]
    
    Interrupts are automatically enabled when requested, so we need to
    initialize irq_enabled accordingly to avoid causing an unbalanced enable
    warning.
    
    Fixes: c62d658e5253 ("rtc: isl12022: Add alarm support")
    Signed-off-by: Esben Haabendal <esben@geanix.com>
    Link: https://lore.kernel.org/r/20250516-rtc-uie-irq-fixes-v2-2-3de8e530a39e@geanix.com
    Signed-off-by: Alexandre Belloni <alexandre.belloni@bootlin.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 47642598958bb43e403ca7c1d908b84392e771f0
Author: Paulo Alcantara <pc@manguebit.org>
Date:   Tue Oct 7 16:23:24 2025 -0300

    smb: client: fix missing timestamp updates after utime(2)
    
    [ Upstream commit b95cd1bdf5aa9221c98fc9259014b8bb8d1829d7 ]
    
    Don't reuse open handle when changing timestamps to prevent the server
    from disabling automatic timestamp updates as per MS-FSA 2.1.4.17.
    
    ---8<---
    import os
    import time
    
    filename = '/mnt/foo'
    
    def print_stat(prefix):
        st = os.stat(filename)
        print(prefix, ': ', time.ctime(st.st_atime), time.ctime(st.st_ctime))
    
    fd = os.open(filename, os.O_CREAT|os.O_TRUNC|os.O_WRONLY, 0o644)
    print_stat('old')
    os.utime(fd, None)
    time.sleep(2)
    os.write(fd, b'foo')
    os.close(fd)
    time.sleep(2)
    print_stat('new')
    ---8<---
    
    Before patch:
    
    $ mount.cifs //srv/share /mnt -o ...
    $ python3 run.py
    old :  Fri Oct  3 14:01:21 2025 Fri Oct  3 14:01:21 2025
    new :  Fri Oct  3 14:01:21 2025 Fri Oct  3 14:01:21 2025
    
    After patch:
    
    $ mount.cifs //srv/share /mnt -o ...
    $ python3 run.py
    old :  Fri Oct  3 17:03:34 2025 Fri Oct  3 17:03:34 2025
    new :  Fri Oct  3 17:03:36 2025 Fri Oct  3 17:03:36 2025
    
    Fixes: b6f2a0f89d7e ("cifs: for compound requests, use open handle if possible")
    Signed-off-by: Paulo Alcantara (Red Hat) <pc@manguebit.org>
    Cc: Frank Sorenson <sorenson@redhat.com>
    Reviewed-by: David Howells <dhowells@redhat.com>
    Cc: linux-cifs@vger.kernel.org
    Signed-off-by: Steve French <stfrench@microsoft.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit c67452431a189c5ba597bff51ac7b8efbc7cfcf3
Author: Fushuai Wang <wangfushuai@baidu.com>
Date:   Tue Oct 7 16:26:03 2025 +0800

    cifs: Fix copy_to_iter return value check
    
    [ Upstream commit 0cc380d0e1d36b8f2703379890e90f896f68e9e8 ]
    
    The return value of copy_to_iter() function will never be negative,
    it is the number of bytes copied, or zero if nothing was copied.
    Update the check to treat 0 as an error, and return -1 in that case.
    
    Fixes: d08089f649a0 ("cifs: Change the I/O paths to use an iterator rather than a page list")
    Acked-by: Tom Talpey <tom@talpey.com>
    Reviewed-by: David Howells <dhowells@redhat.com>
    Signed-off-by: Fushuai Wang <wangfushuai@baidu.com>
    Signed-off-by: Steve French <stfrench@microsoft.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit d8ae3cd5e4051acd376dfd6ceb98a109fc9bef2d
Author: Lorenzo Bianconi <lorenzo@kernel.org>
Date:   Wed Oct 8 11:27:43 2025 +0200

    net: airoha: Fix loopback mode configuration for GDM2 port
    
    [ Upstream commit fea8cdf6738a8b25fccbb7b109b440795a0892cb ]
    
    Add missing configuration for loopback mode in airhoha_set_gdm2_loopback
    routine.
    
    Fixes: 9cd451d414f6e ("net: airoha: Add loopback support for GDM2")
    Signed-off-by: Lorenzo Bianconi <lorenzo@kernel.org>
    Reviewed-by: Jacob Keller <jacob.e.keller@intel.com>
    Link: https://patch.msgid.link/20251008-airoha-loopback-mode-fix-v2-1-045694fe7f60@kernel.org
    Signed-off-by: Paolo Abeni <pabeni@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit da7afb01ba05577ba3629f7f4824205550644986
Author: Herbert Xu <herbert@gondor.apana.org.au>
Date:   Wed Oct 8 15:54:20 2025 +0800

    crypto: essiv - Check ssize for decryption and in-place encryption
    
    [ Upstream commit 6bb73db6948c2de23e407fe1b7ef94bf02b7529f ]
    
    Move the ssize check to the start in essiv_aead_crypt so that
    it's also checked for decryption and in-place encryption.
    
    Reported-by: Muhammad Alifa Ramdhan <ramdhan@starlabs.sg>
    Fixes: be1eb7f78aa8 ("crypto: essiv - create wrapper template for ESSIV generation")
    Signed-off-by: Herbert Xu <herbert@gondor.apana.org.au>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit cf2b35668b808cb08c7490eed5e41b9ef7b5d92d
Author: Pavel Begunkov <asml.silence@gmail.com>
Date:   Wed Oct 8 13:39:01 2025 +0100

    io_uring/zcrx: increment fallback loop src offset
    
    [ Upstream commit e9a9dcb4ccb32446165800a9d83058e95c4833d2 ]
    
    Don't forget to adjust the source offset in io_copy_page(), otherwise
    it'll be copying into the same location in some cases for highmem
    setups.
    
    Fixes: e67645bb7f3f4 ("io_uring/zcrx: prepare fallback for larger pages")
    Signed-off-by: Pavel Begunkov <asml.silence@gmail.com>
    Signed-off-by: Jens Axboe <axboe@kernel.dk>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit a53e849e5dbfae36739000dd7ca5690aa72b9e80
Author: Florian Westphal <fw@strlen.de>
Date:   Thu Oct 2 15:05:41 2025 +0200

    selftests: netfilter: query conntrack state to check for port clash resolution
    
    [ Upstream commit e84945bdc619ed4243ba4298dbb8ca2062026474 ]
    
    Jakub reported this self test flaking occasionally (fails, but passes on
    re-run) on debug kernels.
    
    This is because the test checks for elapsed time to determine if both
    connections were established in parallel.
    
    Rework this to no longer depend on timing.
    Use busywait helper to check that both sockets have moved to established
    state and then query the conntrack engine for the two entries.
    
    Reported-by: Jakub Kicinski <kuba@kernel.org>
    Closes: https://lore.kernel.org/netfilter-devel/20250926163318.40d1a502@kernel.org/
    Fixes: 117e149e26d1 ("selftests: netfilter: test nat source port clash resolution interaction with tcp early demux")
    Signed-off-by: Florian Westphal <fw@strlen.de>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 7ffea2655267ebbaf6a37419c115ac8e90446492
Author: Florian Westphal <fw@strlen.de>
Date:   Thu Oct 2 15:00:06 2025 +0200

    selftests: netfilter: nft_fib.sh: fix spurious test failures
    
    [ Upstream commit a126ab6b26f107f4eb100c8c77e9f10b706f26e6 ]
    
    Jakub reports spurious failure of nft_fib.sh test.
    This is caused by a subtle bug inherited when i moved faulty ping
    from one test case to another.
    
    nft_fib.sh not only checks that the fib expression matched, it also
    records the number of matches and then validates we have the expected
    count.  When I did this it was under the assumption that we would
    have 0 to n matching packets.  In case of the failure, the entry has
    n+1 matching packets.
    
    This happens because ping_unreachable helper uses "ping -c 1 -w 1",
    instead of the intended "-W".  -w alters the meaning of -c (count),
    namely, its then treated as number of wanted *replies* instead of
    "number of packets to send".
    
    So, in some cases, ping -c 1 -w 1 ends up sending two packets which then
    makes the test fail due to the higher-than-expected packet count.
    
    Fix the actual bug (s/-w/-W) and also change the error handling:
    1. Show the number of expected packets in the error message
    2. Always try to delete the key from the set.
       Else, later test that makes sure we don't have unexpected keys
       in there will always fail as well.
    
    Reported-by: Jakub Kicinski <kuba@kernel.org>
    Closes: https://lore.kernel.org/netfilter-devel/20250927090709.0b3cd783@kernel.org/
    Fixes: 98287045c979 ("selftests: netfilter: move fib vrf test to nft_fib.sh")
    Signed-off-by: Florian Westphal <fw@strlen.de>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit d6089b0b7575982b692b8f024c70b5551604946e
Author: Eric Woudstra <ericwouds@gmail.com>
Date:   Tue Oct 7 10:15:01 2025 +0200

    bridge: br_vlan_fill_forward_path_pvid: use br_vlan_group_rcu()
    
    [ Upstream commit bbf0c98b3ad9edaea1f982de6c199cc11d3b7705 ]
    
    net/bridge/br_private.h:1627 suspicious rcu_dereference_protected() usage!
    other info that might help us debug this:
    
    rcu_scheduler_active = 2, debug_locks = 1
    7 locks held by socat/410:
     #0: ffff88800d7a9c90 (sk_lock-AF_INET){+.+.}-{0:0}, at: inet_stream_connect+0x43/0xa0
     #1: ffffffff9a779900 (rcu_read_lock){....}-{1:3}, at: __ip_queue_xmit+0x62/0x1830
     [..]
     #6: ffffffff9a779900 (rcu_read_lock){....}-{1:3}, at: nf_hook.constprop.0+0x8a/0x440
    
    Call Trace:
     lockdep_rcu_suspicious.cold+0x4f/0xb1
     br_vlan_fill_forward_path_pvid+0x32c/0x410 [bridge]
     br_fill_forward_path+0x7a/0x4d0 [bridge]
    
    Use to correct helper, non _rcu variant requires RTNL mutex.
    
    Fixes: bcf2766b1377 ("net: bridge: resolve forwarding path for VLAN tag actions in bridge devices")
    Signed-off-by: Eric Woudstra <ericwouds@gmail.com>
    Signed-off-by: Florian Westphal <fw@strlen.de>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 4c1cf72ec10be5a9ad264650cadffa1fbce6fabd
Author: Fernando Fernandez Mancera <fmancera@suse.de>
Date:   Wed Oct 8 12:08:16 2025 +0200

    netfilter: nft_objref: validate objref and objrefmap expressions
    
    [ Upstream commit f359b809d54c6e3dd1d039b97e0b68390b0e53e4 ]
    
    Referencing a synproxy stateful object from OUTPUT hook causes kernel
    crash due to infinite recursive calls:
    
    BUG: TASK stack guard page was hit at 000000008bda5b8c (stack is 000000003ab1c4a5..00000000494d8b12)
    [...]
    Call Trace:
     __find_rr_leaf+0x99/0x230
     fib6_table_lookup+0x13b/0x2d0
     ip6_pol_route+0xa4/0x400
     fib6_rule_lookup+0x156/0x240
     ip6_route_output_flags+0xc6/0x150
     __nf_ip6_route+0x23/0x50
     synproxy_send_tcp_ipv6+0x106/0x200
     synproxy_send_client_synack_ipv6+0x1aa/0x1f0
     nft_synproxy_do_eval+0x263/0x310
     nft_do_chain+0x5a8/0x5f0 [nf_tables
     nft_do_chain_inet+0x98/0x110
     nf_hook_slow+0x43/0xc0
     __ip6_local_out+0xf0/0x170
     ip6_local_out+0x17/0x70
     synproxy_send_tcp_ipv6+0x1a2/0x200
     synproxy_send_client_synack_ipv6+0x1aa/0x1f0
    [...]
    
    Implement objref and objrefmap expression validate functions.
    
    Currently, only NFT_OBJECT_SYNPROXY object type requires validation.
    This will also handle a jump to a chain using a synproxy object from the
    OUTPUT hook.
    
    Now when trying to reference a synproxy object in the OUTPUT hook, nft
    will produce the following error:
    
    synproxy_crash.nft: Error: Could not process rule: Operation not supported
      synproxy name mysynproxy
      ^^^^^^^^^^^^^^^^^^^^^^^^
    
    Fixes: ee394f96ad75 ("netfilter: nft_synproxy: add synproxy stateful object support")
    Reported-by: Georg Pfuetzenreuter <georg.pfuetzenreuter@suse.com>
    Closes: https://bugzilla.suse.com/1250237
    Signed-off-by: Fernando Fernandez Mancera <fmancera@suse.de>
    Reviewed-by: Pablo Neira Ayuso <pablo@netfilter.org>
    Signed-off-by: Florian Westphal <fw@strlen.de>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit f041339d6b9a5a46437f0c48fc7279c92af7a513
Author: T Pratham <t-pratham@ti.com>
Date:   Tue Oct 7 19:27:51 2025 +0530

    crypto: skcipher - Fix reqsize handling
    
    [ Upstream commit 229c586b5e86979badb7cb0d38717b88a9e95ddd ]
    
    Commit afddce13ce81d ("crypto: api - Add reqsize to crypto_alg")
    introduced cra_reqsize field in crypto_alg struct to replace type
    specific reqsize fields. It looks like this was introduced specifically
    for ahash and acomp from the commit description as subsequent commits
    add necessary changes in these alg frameworks.
    
    However, this is being recommended for use in all crypto algs [1]
    instead of setting reqsize using crypto_*_set_reqsize(). Using
    cra_reqsize in skcipher algorithms, hence, causes memory
    corruptions and crashes as the underlying functions in the algorithm
    framework have not been updated to set the reqsize properly from
    cra_reqsize. [2]
    
    Add proper set_reqsize calls in the skcipher init function to
    properly initialize reqsize for these algorithms in the framework.
    
    [1]: https://lore.kernel.org/linux-crypto/aCL8BxpHr5OpT04k@gondor.apana.org.au/
    [2]: https://gist.github.com/Pratham-T/24247446f1faf4b7843e4014d5089f6b
    
    Fixes: afddce13ce81d ("crypto: api - Add reqsize to crypto_alg")
    Fixes: 52f641bc63a4 ("crypto: ti - Add driver for DTHE V2 AES Engine (ECB, CBC)")
    Signed-off-by: T Pratham <t-pratham@ti.com>
    Signed-off-by: Herbert Xu <herbert@gondor.apana.org.au>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit cb71007c4d1610d6fd65470372e266b2d7ed3b57
Author: Thomas Wismer <thomas.wismer@scs.ch>
Date:   Mon Oct 6 22:40:29 2025 +0200

    net: pse-pd: tps23881: Fix current measurement scaling
    
    [ Upstream commit 2c95a756e0cfc19af6d0b32b0c6cf3bada334998 ]
    
    The TPS23881 improves on the TPS23880 with current sense resistors reduced
    from 255 mOhm to 200 mOhm. This has a direct impact on the scaling of the
    current measurement. However, the latest TPS23881 data sheet from May 2023
    still shows the scaling of the TPS23880 model.
    
    Fixes: 7f076ce3f1733 ("net: pse-pd: tps23881: Add support for power limit and measurement features")
    Signed-off-by: Thomas Wismer <thomas.wismer@scs.ch>
    Acked-by: Kory Maincent <kory.maincent@bootlin.com>
    Link: https://patch.msgid.link/20251006204029.7169-2-thomas@wismer.xyz
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 60f6112fc9b3ba0eae519f10702c0c13bab45742
Author: Philip Yang <Philip.Yang@amd.com>
Date:   Tue May 27 11:09:53 2025 -0400

    drm/amdkfd: Fix kfd process ref leaking when userptr unmapping
    
    [ Upstream commit 58e6fc2fb94f0f409447e5d46cf6a417b6397fbc ]
    
    kfd_lookup_process_by_pid hold the kfd process reference to ensure it
    doesn't get destroyed while sending the segfault event to user space.
    
    Calling kfd_lookup_process_by_pid as function parameter leaks the kfd
    process refcount and miss the NULL pointer check if app process is
    already destroyed.
    
    Fixes: 2d274bf7099b ("amd/amdkfd: Trigger segfault for early userptr unmmapping")
    Signed-off-by: Philip Yang <Philip.Yang@amd.com>
    Reviewed-by: Harish Kasiviswanathan <Harish.Kasiviswanathan@amd.com>
    Signed-off-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 842e6c4032406b2eea8bed3588557b468fe397e8
Author: Timur Kristóf <timur.kristof@gmail.com>
Date:   Thu Sep 25 20:45:25 2025 +0200

    drm/amd/display: Disable scaling on DCE6 for now
    
    [ Upstream commit 0e190a0446ec517666dab4691b296a9b758e590f ]
    
    Scaling doesn't work on DCE6 at the moment, the current
    register programming produces incorrect output when using
    fractional scaling (between 100-200%) on resolutions higher
    than 1080p.
    
    Disable it until we figure out how to program it properly.
    
    Fixes: 7c15fd86aaec ("drm/amd/display: dc/dce: add initial DCE6 support (v10)")
    Reviewed-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Timur Kristóf <timur.kristof@gmail.com>
    Signed-off-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit e73202601f29ad7703c48d4076a4fc1a27e39726
Author: Timur Kristóf <timur.kristof@gmail.com>
Date:   Thu Sep 25 20:45:24 2025 +0200

    drm/amd/display: Properly disable scaling on DCE6
    
    [ Upstream commit a7dc87f3448bea5ebe054f14e861074b9c289c65 ]
    
    SCL_SCALER_ENABLE can be used to enable/disable the scaler
    on DCE6. Program it to 0 when scaling isn't used, 1 when used.
    Additionally, clear some other registers when scaling is
    disabled and program the SCL_UPDATE register as recommended.
    
    This fixes visible glitches for users whose BIOS sets up a
    mode with scaling at boot, which DC was unable to clean up.
    
    Fixes: b70aaf5586f2 ("drm/amd/display: dce_transform: add DCE6 specific macros,functions")
    Reviewed-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Timur Kristóf <timur.kristof@gmail.com>
    Signed-off-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit e4dbb75f49986fa5526fac580ce91e0621036cc8
Author: Timur Kristóf <timur.kristof@gmail.com>
Date:   Thu Sep 25 20:45:23 2025 +0200

    drm/amd/display: Properly clear SCL_*_FILTER_CONTROL on DCE6
    
    [ Upstream commit c0aa7cf49dd6cb302fe28e7183992b772cb7420c ]
    
    Previously, the code would set a bit field which didn't exist
    on DCE6 so it would be effectively a no-op.
    
    Fixes: b70aaf5586f2 ("drm/amd/display: dce_transform: add DCE6 specific macros,functions")
    Reviewed-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Timur Kristóf <timur.kristof@gmail.com>
    Signed-off-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit c19ed1a62d339045ef6b5e7c499094f4214c7f74
Author: Timur Kristóf <timur.kristof@gmail.com>
Date:   Thu Sep 25 20:45:22 2025 +0200

    drm/amd/display: Add missing DCE6 SCL_HORZ_FILTER_INIT* SRIs
    
    [ Upstream commit d60f9c45d1bff7e20ecd57492ef7a5e33c94a37c ]
    
    Without these, it's impossible to program these registers.
    
    Fixes: 102b2f587ac8 ("drm/amd/display: dce_transform: DCE6 Scaling Horizontal Filter Init (v2)")
    Reviewed-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Timur Kristóf <timur.kristof@gmail.com>
    Signed-off-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 4700d417d0aec017c31a49c8dd2f52ab0176eae4
Author: Alex Deucher <alexander.deucher@amd.com>
Date:   Thu Sep 25 20:45:21 2025 +0200

    drm/amdgpu: Add additional DCE6 SCL registers
    
    [ Upstream commit 507296328b36ffd00ec1f4fde5b8acafb7222ec7 ]
    
    Fixes: 102b2f587ac8 ("drm/amd/display: dce_transform: DCE6 Scaling Horizontal Filter Init (v2)")
    Signed-off-by: Alex Deucher <alexander.deucher@amd.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 37ce5a4207616536a7e09e20f2a9ff7a5527a49f
Author: Jason-JH Lin <jason-jh.lin@mediatek.com>
Date:   Fri Aug 29 17:15:58 2025 +0800

    mailbox: mtk-cmdq: Remove pm_runtime APIs from cmdq_mbox_send_data()
    
    [ Upstream commit 3f39f56520374cf56872644acf9afcc618a4b674 ]
    
    pm_runtime_get_sync() and pm_runtime_put_autosuspend() were previously
    called in cmdq_mbox_send_data(), which is under a spinlock in msg_submit()
    (mailbox.c). This caused lockdep warnings such as "sleeping function
    called from invalid context" when running with lockdebug enabled.
    
    The BUG report:
      BUG: sleeping function called from invalid context at drivers/base/power/runtime.c:1164
      in_atomic(): 1, irqs_disabled(): 128, non_block: 0, pid: 3616, name: kworker/u17:3
        preempt_count: 1, expected: 0
        RCU nest depth: 0, expected: 0
        INFO: lockdep is turned off.
        irq event stamp: 0
        CPU: 1 PID: 3616 Comm: kworker/u17:3 Not tainted 6.1.87-lockdep-14133-g26e933aca785 #1
        Hardware name: Google Ciri sku0/unprovisioned board (DT)
        Workqueue: imgsys_runner imgsys_runner_func
        Call trace:
         dump_backtrace+0x100/0x120
         show_stack+0x20/0x2c
         dump_stack_lvl+0x84/0xb4
         dump_stack+0x18/0x48
         __might_resched+0x354/0x4c0
         __might_sleep+0x98/0xe4
         __pm_runtime_resume+0x70/0x124
         cmdq_mbox_send_data+0xe4/0xb1c
         msg_submit+0x194/0x2dc
         mbox_send_message+0x190/0x330
         imgsys_cmdq_sendtask+0x1618/0x2224
         imgsys_runner_func+0xac/0x11c
         process_one_work+0x638/0xf84
         worker_thread+0x808/0xcd0
         kthread+0x24c/0x324
         ret_from_fork+0x10/0x20
    
    Additionally, pm_runtime_put_autosuspend() should be invoked from the
    GCE IRQ handler to ensure the hardware has actually completed its work.
    
    To resolve these issues, remove the pm_runtime calls from
    cmdq_mbox_send_data() and delegate power management responsibilities
    to the client driver.
    
    Fixes: 8afe816b0c99 ("mailbox: mtk-cmdq-mailbox: Implement Runtime PM with autosuspend")
    Signed-off-by: Jason-JH Lin <jason-jh.lin@mediatek.com>
    Signed-off-by: Jassi Brar <jassisinghbrar@gmail.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 993c4ba71596c30418ba5a0ddcf4f9c2f431466a
Author: Carolina Jubran <cjubran@nvidia.com>
Date:   Sun Oct 5 11:29:58 2025 +0300

    net/mlx5e: Prevent tunnel reformat when tunnel mode not allowed
    
    [ Upstream commit 22239eb258bc1e6ccdb2d3502fce1cc2b2a88386 ]
    
    When configuring IPsec packet offload in tunnel mode, the driver tries
    to create tunnel reformat objects unconditionally. This is incorrect,
    because tunnel mode is only permitted under specific encapsulation
    settings, and that decision is already made when the flow table is
    created.
    
    The offending commit attempted to block this case in the state add
    path, but the check there happens too late and does not prevent the
    reformat from being configured.
    
    Fix by taking short reservations for both the eswitch mode and the
    encap at the start of state setup. This preserves the block ordering
    (mode --> encap) used later: the mode is blocked during RX/TX get, and
    the encap is blocked during flow-table creation. This lets us fail
    early if either reservation cannot be obtained, it means a mode
    transition is underway or a conflicting configuration already owns
    encap. If both succeed, the flow-table path later takes the ownership
    and the reservations are released on exit.
    
    Fixes: 146c196b60e4 ("net/mlx5e: Create IPsec table with tunnel support only when encap is disabled")
    Signed-off-by: Carolina Jubran <cjubran@nvidia.com>
    Reviewed-by: Jianbo Liu <jianbol@nvidia.com>
    Reviewed-by: Leon Romanovsky <leonro@nvidia.com>
    Signed-off-by: Tariq Toukan <tariqt@nvidia.com>
    Link: https://patch.msgid.link/1759652999-858513-3-git-send-email-tariqt@nvidia.com
    Signed-off-by: Paolo Abeni <pabeni@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit b56aee2c3ed5ad6ad97006a1fb21ac4993488abb
Author: Carolina Jubran <cjubran@nvidia.com>
Date:   Sun Oct 5 11:29:57 2025 +0300

    net/mlx5: Prevent tunnel mode conflicts between FDB and NIC IPsec tables
    
    [ Upstream commit 7593439c13933164f701eed9c83d89358f203469 ]
    
    When creating IPsec flow tables with tunnel mode enabled, the driver
    uses mlx5_eswitch_block_encap() to prevent tunnel encapsulation
    conflicts across different domains (NIC_RX/NIC_TX and FDB), since the
    firmware doesn’t allow both at the same time.
    
    Currently, the driver attempts to reserve tunnel mode unconditionally
    for both NIC and FDB IPsec tables. This can lead to conflicting tunnel
    mode setups, for example, if a flow table was created in the FDB
    domain with tunnel offload enabled, and we later try to create another
    one in the NIC, or vice versa.
    
    To resolve this, adjust the blocking logic so that tunnel mode is only
    reserved by NIC flows. This ensures that tunnel offload is exclusively
    used in either the NIC or the FDB, and avoids unintended offload
    conflicts.
    
    Fixes: 1762f132d542 ("net/mlx5e: Support IPsec packet offload for RX in switchdev mode")
    Fixes: c6c2bf5db4ea ("net/mlx5e: Support IPsec packet offload for TX in switchdev mode")
    Signed-off-by: Carolina Jubran <cjubran@nvidia.com>
    Reviewed-by: Jianbo Liu <jianbol@nvidia.com>
    Reviewed-by: Leon Romanovsky <leonro@nvidia.com>
    Signed-off-by: Tariq Toukan <tariqt@nvidia.com>
    Link: https://patch.msgid.link/1759652999-858513-2-git-send-email-tariqt@nvidia.com
    Signed-off-by: Paolo Abeni <pabeni@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 20883557dc90d95b38e3f1a6ac90514c8c612103
Author: Daniel Machon <daniel.machon@microchip.com>
Date:   Fri Oct 3 14:35:59 2025 +0200

    net: sparx5/lan969x: fix flooding configuration on bridge join/leave
    
    [ Upstream commit c9d1b0b54258ba13b567dd116ead3c7c30cba7d8 ]
    
    The sparx5 driver programs UC/MC/BC flooding in sparx5_update_fwd() by
    unconditionally applying bridge_fwd_mask to all flood PGIDs. Any bridge
    topology change that triggers sparx5_update_fwd() (for example enslaving
    another port) therefore reinstalls flooding in hardware for already
    bridged ports, regardless of their per-port flood flags.
    
    This results in clobbering of the flood masks, and desynchronization
    between software and hardware: the bridge still reports “flood off” for
    the port, but hardware has flooding enabled due to unconditional PGID
    reprogramming.
    
    Steps to reproduce:
    
        $ ip link add br0 type bridge
        $ ip link set br0 up
        $ ip link set eth0 master br0
        $ ip link set eth0 up
        $ bridge link set dev eth0 flood off
        $ ip link set eth1 master br0
        $ ip link set eth1 up
    
    At this point, flooding is silently re-enabled for eth0. Software still
    shows “flood off” for eth0, but hardware has flooding enabled.
    
    To fix this, flooding is now set explicitly during bridge join/leave,
    through sparx5_port_attr_bridge_flags():
    
        On bridge join, UC/MC/BC flooding is enabled by default.
    
        On bridge leave, UC/MC/BC flooding is disabled.
    
        sparx5_update_fwd() no longer touches the flood PGIDs, clobbering
        the flood masks, and desynchronizing software and hardware.
    
        Initialization of the flooding PGIDs have been moved to
        sparx5_start(). This is required as flooding PGIDs defaults to
        0x3fffffff in hardware and the initialization was previously handled
        in sparx5_update_fwd(), which was removed.
    
    With this change, user-configured flooding flags persist across bridge
    updates and are no longer overridden by sparx5_update_fwd().
    
    Fixes: d6fce5141929 ("net: sparx5: add switching support")
    Signed-off-by: Daniel Machon <daniel.machon@microchip.com>
    Reviewed-by: Simon Horman <horms@kernel.org>
    Link: https://patch.msgid.link/20251003-fix-flood-fwd-v1-1-48eb478b2904@microchip.com
    Signed-off-by: Paolo Abeni <pabeni@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit a1ae2839298ad0164e7f8b8d44542c7f9ea28bbb
Author: Maxime Chevallier <maxime.chevallier@bootlin.com>
Date:   Fri Oct 3 09:03:06 2025 +0200

    net: mdio: mdio-i2c: Hold the i2c bus lock during smbus transactions
    
    [ Upstream commit 4dc8b26a3ac2cb79f19f252d9077696d3ef0823a ]
    
    When accessing an MDIO register using single-byte smbus accesses, we have to
    perform 2 consecutive operations targeting the same address,
    first accessing the MSB then the LSB of the 16 bit register:
    
      read_1_byte(addr); <- returns MSB of register at address 'addr'
      read_1_byte(addr); <- returns LSB
    
    Some PHY devices present in SFP such as the Broadcom 5461 don't like
    seeing foreign i2c transactions in-between these 2 smbus accesses, and
    will return the MSB a second time when trying to read the LSB :
    
      read_1_byte(addr); <- returns MSB
    
            i2c_transaction_for_other_device_on_the_bus();
    
      read_1_byte(addr); <- returns MSB again
    
    Given the already fragile nature of accessing PHYs/SFPs with single-byte
    smbus accesses, it's safe to say that this Broadcom PHY may not be the
    only one acting like this.
    
    Let's therefore hold the i2c bus lock while performing our smbus
    transactions to avoid interleaved accesses.
    
    Fixes: d4bd3aca33c2 ("net: mdio: mdio-i2c: Add support for single-byte SMBus operations")
    Signed-off-by: Maxime Chevallier <maxime.chevallier@bootlin.com>
    Reviewed-by: Kory Maincent <kory.maincent@bootlin.com>
    Reviewed-by: Andrew Lunn <andrew@lunn.ch>
    Link: https://patch.msgid.link/20251003070311.861135-1-maxime.chevallier@bootlin.com
    Signed-off-by: Paolo Abeni <pabeni@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 7404ce888a45eb7da0508b7cbbe6f2e95302eeb8
Author: Daniel Borkmann <daniel@iogearbox.net>
Date:   Fri Oct 3 09:34:18 2025 +0200

    bpf: Fix metadata_dst leak __bpf_redirect_neigh_v{4,6}
    
    [ Upstream commit 23f3770e1a53e6c7a553135011f547209e141e72 ]
    
    Cilium has a BPF egress gateway feature which forces outgoing K8s Pod
    traffic to pass through dedicated egress gateways which then SNAT the
    traffic in order to interact with stable IPs outside the cluster.
    
    The traffic is directed to the gateway via vxlan tunnel in collect md
    mode. A recent BPF change utilized the bpf_redirect_neigh() helper to
    forward packets after the arrival and decap on vxlan, which turned out
    over time that the kmalloc-256 slab usage in kernel was ever-increasing.
    
    The issue was that vxlan allocates the metadata_dst object and attaches
    it through a fake dst entry to the skb. The latter was never released
    though given bpf_redirect_neigh() was merely setting the new dst entry
    via skb_dst_set() without dropping an existing one first.
    
    Fixes: b4ab31414970 ("bpf: Add redirect_neigh helper as redirect drop-in")
    Reported-by: Yusuke Suzuki <yusuke.suzuki@isovalent.com>
    Reported-by: Julian Wiedmann <jwi@isovalent.com>
    Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
    Cc: Martin KaFai Lau <martin.lau@kernel.org>
    Cc: Jakub Kicinski <kuba@kernel.org>
    Cc: Jordan Rife <jrife@google.com>
    Reviewed-by: Simon Horman <horms@kernel.org>
    Reviewed-by: Jordan Rife <jrife@google.com>
    Reviewed-by: Jakub Kicinski <kuba@kernel.org>
    Reviewed-by: Martin KaFai Lau <martin.lau@kernel.org>
    Link: https://lore.kernel.org/r/20251003073418.291171-1-daniel@iogearbox.net
    Signed-off-by: Alexei Starovoitov <ast@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 32bf7c6e01f5ba17a53ba236a770bd0274cefdf4
Author: Harini T <harini.t@amd.com>
Date:   Mon Sep 29 13:07:23 2025 +0530

    mailbox: zynqmp-ipi: Fix SGI cleanup on unbind
    
    [ Upstream commit bb160e791ab15b89188a7a19589b8e11f681bef3 ]
    
    The driver incorrectly determines SGI vs SPI interrupts by checking IRQ
    number < 16, which fails with dynamic IRQ allocation. During unbind,
    this causes improper SGI cleanup leading to kernel crash.
    
    Add explicit irq_type field to pdata for reliable identification of SGI
    interrupts (type-2) and only clean up SGI resources when appropriate.
    
    Fixes: 6ffb1635341b ("mailbox: zynqmp: handle SGI for shared IPI")
    Signed-off-by: Harini T <harini.t@amd.com>
    Reviewed-by: Peng Fan <peng.fan@nxp.com>
    Signed-off-by: Jassi Brar <jassisinghbrar@gmail.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit ab96f08ecedd263ecaab9df8455bfb23b07fdcc2
Author: Harini T <harini.t@amd.com>
Date:   Mon Sep 29 13:07:22 2025 +0530

    mailbox: zynqmp-ipi: Fix out-of-bounds access in mailbox cleanup loop
    
    [ Upstream commit 0aead8197fc1a85b0a89646e418feb49a564b029 ]
    
    The cleanup loop was starting at the wrong array index, causing
    out-of-bounds access.
    Start the loop at the correct index for zero-indexed arrays to prevent
    accessing memory beyond the allocated array bounds.
    
    Fixes: 4981b82ba2ff ("mailbox: ZynqMP IPI mailbox controller")
    Signed-off-by: Harini T <harini.t@amd.com>
    Reviewed-by: Peng Fan <peng.fan@nxp.com>
    Signed-off-by: Jassi Brar <jassisinghbrar@gmail.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 66ca91400d7718803aeb9a18b57ff6632e103b77
Author: Harini T <harini.t@amd.com>
Date:   Mon Sep 29 13:07:21 2025 +0530

    mailbox: zynqmp-ipi: Remove dev.parent check in zynqmp_ipi_free_mboxes
    
    [ Upstream commit 019e3f4550fc7d319a7fd03eff487255f8e8aecd ]
    
    The ipi_mbox->dev.parent check is unreliable proxy for registration
    status as it fails to protect against probe failures that occur after
    the parent is assigned but before device_register() completes.
    
    device_is_registered() is the canonical and robust method to verify the
    registration status.
    
    Remove ipi_mbox->dev.parent check in zynqmp_ipi_free_mboxes().
    
    Fixes: 4981b82ba2ff ("mailbox: ZynqMP IPI mailbox controller")
    Signed-off-by: Harini T <harini.t@amd.com>
    Reviewed-by: Peng Fan <peng.fan@nxp.com>
    Signed-off-by: Jassi Brar <jassisinghbrar@gmail.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 87b0740b35cfff5a5ff5c4c6d6df373182127fcc
Author: Harini T <harini.t@amd.com>
Date:   Mon Sep 29 13:07:20 2025 +0530

    mailbox: zynqmp-ipi: Remove redundant mbox_controller_unregister() call
    
    [ Upstream commit 341867f730d3d3bb54491ee64e8b1a0c446656e7 ]
    
    The controller is registered using the device-managed function
    'devm_mbox_controller_register()'. As documented in mailbox.c, this
    ensures the devres framework automatically calls
    mbox_controller_unregister() when device_unregister() is invoked, making
    the explicit call unnecessary.
    
    Remove redundant mbox_controller_unregister() call as
    device_unregister() handles controller cleanup.
    
    Fixes: 4981b82ba2ff ("mailbox: ZynqMP IPI mailbox controller")
    Signed-off-by: Harini T <harini.t@amd.com>
    Reviewed-by: Peng Fan <peng.fan@nxp.com>
    Signed-off-by: Jassi Brar <jassisinghbrar@gmail.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 0e789f86fbb30a21f26137146f887c96ab8e91b7
Author: Vincent Minet <v.minet@criteo.com>
Date:   Mon Sep 22 07:37:02 2025 +0200

    perf tools: Fix arm64 libjvmti build by generating unistd_64.h
    
    [ Upstream commit f3b601f900902ab80902c44f820a8985384ac021 ]
    
    Since commit 22f72088ffe6 ("tools headers: Update the syscall table with
    the kernel sources") the arm64 syscall header is generated at build
    time. Later, commit bfb713ea53c7 ("perf tools: Fix arm64 build by
    generating unistd_64.h") added a dependency to libperf to guarantee that
    this header was created before building libperf or perf itself.
    
    However, libjvmti also requires this header but does not depend on
    libperf, leading to build failures such as:
    
      In file included from /usr/include/sys/syscall.h:24,
                       from /usr/include/syscall.h:1,
                       from jvmti/jvmti_agent.c:36:
      tools/arch/arm64/include/uapi/asm/unistd.h:2:10: fatal error: asm/unistd_64.h: No such file or directory
          2 | #include <asm/unistd_64.h>
    
    Fix this by ensuring that libperf is built before libjvmti, so that
    unistd_64.h is always available.
    
    Fixes: 22f72088ffe69a37 ("tools headers: Update the syscall table with the kernel sources")
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Vincent Minet <v.minet@criteo.com>
    Link: https://lore.kernel.org/r/20250922053702.2688374-1-v.minet@criteo.com
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit fbe6af6d82eda518ad654cfee91bf6f238c7172f
Author: Eric Dumazet <edumazet@google.com>
Date:   Fri Oct 3 18:41:19 2025 +0000

    tcp: take care of zero tp->window_clamp in tcp_set_rcvlowat()
    
    [ Upstream commit 21b29e74ffe5a6c851c235bb80bf5ee26292c67b ]
    
    Some applications (like selftests/net/tcp_mmap.c) call SO_RCVLOWAT
    on their listener, before accept().
    
    This has an unfortunate effect on wscale selection in
    tcp_select_initial_window() during 3WHS.
    
    For instance, tcp_mmap was negotiating wscale 4, regardless
    of tcp_rmem[2] and sysctl_rmem_max.
    
    Do not change tp->window_clamp if it is zero
    or bigger than our computed value.
    
    Zero value is special, it allows tcp_select_initial_window()
    to enable autotuning.
    
    Note that SO_RCVLOWAT use on listener is probably not wise,
    because tp->scaling_ratio has a default value, possibly wrong.
    
    Fixes: d1361840f8c5 ("tcp: fix SO_RCVLOWAT and RCVBUF autotuning")
    Signed-off-by: Eric Dumazet <edumazet@google.com>
    Reviewed-by: Kuniyuki Iwashima <kuniyu@google.com>
    Reviewed-by: Neal Cardwell <ncardwell@google.com>
    Link: https://patch.msgid.link/20251003184119.2526655-1-edumazet@google.com
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 17ba24908e5e730f0396ffc6e4948fe799563ffc
Author: Leo Yan <leo.yan@arm.com>
Date:   Mon Oct 6 17:21:24 2025 +0100

    perf python: split Clang options when invoking Popen
    
    [ Upstream commit c6a43bc3e8f6102a47da0d2e53428d08f00172fb ]
    
    When passing a list to subprocess.Popen, each element maps to one argv
    token. Current code bundles multiple Clang flags into a single element,
    something like:
    
      cmd = ['clang',
             '--target=x86_64-linux-gnu -fintegrated-as -Wno-cast-function-type-mismatch',
             'test-hello.c']
    
    So Clang only sees one long, invalid option instead of separate flags,
    as a result, the script cannot capture any log via PIPE.
    
    Fix this by using shlex.split() to separate the string so each option
    becomes its own argv element. The fixed list will be:
    
      cmd = ['clang',
             '--target=x86_64-linux-gnu',
             '-fintegrated-as',
             '-Wno-cast-function-type-mismatch',
             'test-hello.c']
    
    Fixes: 09e6f9f98370 ("perf python: Fix splitting CC into compiler and options")
    Signed-off-by: Leo Yan <leo.yan@arm.com>
    Reviewed-by: Ian Rogers <irogers@google.com>
    Link: https://lore.kernel.org/r/20251006-perf_build_android_ndk-v3-2-4305590795b2@arm.com
    Cc: Palmer Dabbelt <palmer@dabbelt.com>
    Cc: Albert Ou <aou@eecs.berkeley.edu>
    Cc: Alexandre Ghiti <alex@ghiti.fr>
    Cc: Nick Desaulniers <nick.desaulniers+lkml@gmail.com>
    Cc: Justin Stitt <justinstitt@google.com>
    Cc: Bill Wendling <morbo@google.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Arnaldo Carvalho de Melo <acme@kernel.org>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Nathan Chancellor <nathan@kernel.org>
    Cc: James Clark <james.clark@linaro.org>
    Cc: linux-riscv@lists.infradead.org
    Cc: llvm@lists.linux.dev
    Cc: Paul Walmsley <paul.walmsley@sifive.com>
    Cc: linux-kernel@vger.kernel.org
    Cc: linux-perf-users@vger.kernel.org
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 45f34ae904c5392e16c010f7398f7073b52b4847
Author: Leo Yan <leo.yan@arm.com>
Date:   Mon Oct 6 17:21:23 2025 +0100

    tools build: Align warning options with perf
    
    [ Upstream commit 53d067feb8c4f16d1f24ce3f4df4450bb18c555f ]
    
    The feature test programs are built without enabling '-Wall -Werror'
    options. As a result, a feature may appear to be available, but later
    building in perf can fail with stricter checks.
    
    Make the feature test program use the same warning options as perf.
    
    Fixes: 1925459b4d92 ("tools build: Fix feature Makefile issues with 'O='")
    Signed-off-by: Leo Yan <leo.yan@arm.com>
    Reviewed-by: Ian Rogers <irogers@google.com>
    Link: https://lore.kernel.org/r/20251006-perf_build_android_ndk-v3-1-4305590795b2@arm.com
    Cc: Palmer Dabbelt <palmer@dabbelt.com>
    Cc: Albert Ou <aou@eecs.berkeley.edu>
    Cc: Alexandre Ghiti <alex@ghiti.fr>
    Cc: Nick Desaulniers <nick.desaulniers+lkml@gmail.com>
    Cc: Justin Stitt <justinstitt@google.com>
    Cc: Bill Wendling <morbo@google.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Arnaldo Carvalho de Melo <acme@kernel.org>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Nathan Chancellor <nathan@kernel.org>
    Cc: James Clark <james.clark@linaro.org>
    Cc: linux-riscv@lists.infradead.org
    Cc: llvm@lists.linux.dev
    Cc: Paul Walmsley <paul.walmsley@sifive.com>
    Cc: linux-kernel@vger.kernel.org
    Cc: linux-perf-users@vger.kernel.org
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 620e09727b084537c9d5b84aa48e5ed35dd65c7c
Author: Erick Karanja <karanja99erick@gmail.com>
Date:   Thu Oct 2 20:46:17 2025 +0300

    net: fsl_pq_mdio: Fix device node reference leak in fsl_pq_mdio_probe
    
    [ Upstream commit 521405cb54cd2812bbb6dedd5afc14bca1e7e98a ]
    
    Add missing of_node_put call to release device node tbi obtained
    via for_each_child_of_node.
    
    Fixes: afae5ad78b342 ("net/fsl_pq_mdio: streamline probing of MDIO nodes")
    Signed-off-by: Erick Karanja <karanja99erick@gmail.com>
    Link: https://patch.msgid.link/20251002174617.960521-1-karanja99erick@gmail.com
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 794abb265de3e792167fe3ea0440c064c722bb84
Author: Haotian Zhang <vulab@iscas.ac.cn>
Date:   Wed Oct 1 19:53:36 2025 +0800

    ice: ice_adapter: release xa entry on adapter allocation failure
    
    [ Upstream commit 2db687f3469dbc5c59bc53d55acafd75d530b497 ]
    
    When ice_adapter_new() fails, the reserved XArray entry created by
    xa_insert() is not released. This causes subsequent insertions at
    the same index to return -EBUSY, potentially leading to
    NULL pointer dereferences.
    
    Reorder the operations as suggested by Przemek Kitszel:
    1. Check if adapter already exists (xa_load)
    2. Reserve the XArray slot (xa_reserve)
    3. Allocate the adapter (ice_adapter_new)
    4. Store the adapter (xa_store)
    
    Fixes: 0f0023c649c7 ("ice: do not init struct ice_adapter more times than needed")
    Suggested-by: Przemek Kitszel <przemyslaw.kitszel@intel.com>
    Suggested-by: Jacob Keller <jacob.e.keller@intel.com>
    Signed-off-by: Haotian Zhang <vulab@iscas.ac.cn>
    Reviewed-by: Aleksandr Loktionov <aleksandr.loktionov@intel.com>
    Reviewed-by: Jacob Keller <jacob.e.keller@intel.com>
    Link: https://patch.msgid.link/20251001115336.1707-1-vulab@iscas.ac.cn
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 1eb3b6377d30cf63f8f46f94f69d5c13ebae1412
Author: Sidharth Seela <sidharthseela@gmail.com>
Date:   Wed Oct 1 18:01:08 2025 +0530

    selftest: net: ovpn: Fix uninit return values
    
    [ Upstream commit 7fc25c5a5ae6230d14b4c088fc94dbd58b2a9f3a ]
    
    Fix functions that return undefined values. These issues were caught by
    running clang using LLVM=1 option.
    
    Clang warnings are as follows:
    ovpn-cli.c:1587:6: warning: variable 'ret' is used uninitialized whenever 'if' condition is true [-Wsometimes-uninitialized]
     1587 |         if (!sock) {
          |             ^~~~~
    ovpn-cli.c:1635:9: note: uninitialized use occurs here
     1635 |         return ret;
          |                ^~~
    ovpn-cli.c:1587:2: note: remove the 'if' if its condition is always false
     1587 |         if (!sock) {
          |         ^~~~~~~~~~~~
     1588 |                 fprintf(stderr, "cannot allocate netlink socket\n");
          |                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     1589 |                 goto err_free;
          |                 ~~~~~~~~~~~~~~
     1590 |         }
          |         ~
    ovpn-cli.c:1584:15: note: initialize the variable 'ret' to silence this warning
     1584 |         int mcid, ret;
          |                      ^
          |                       = 0
    ovpn-cli.c:2107:7: warning: variable 'ret' is used uninitialized whenever switch case is taken [-Wsometimes-uninitialized]
     2107 |         case CMD_INVALID:
          |              ^~~~~~~~~~~
    ovpn-cli.c:2111:9: note: uninitialized use occurs here
     2111 |         return ret;
          |                ^~~
    ovpn-cli.c:1939:12: note: initialize the variable 'ret' to silence this warning
     1939 |         int n, ret;
          |                   ^
          |
    
    Fixes: 959bc330a439 ("testing/selftests: add test tool and scripts for ovpn module")
    Signed-off-by: Sidharth Seela <sidharthseela@gmail.com>
    Link: https://patch.msgid.link/20251001123107.96244-2-sidharthseela@gmail.com
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit c3363db5d0685a8d077ade706051bbccc75f7e14
Author: Duoming Zhou <duoming@zju.edu.cn>
Date:   Wed Oct 1 09:11:49 2025 +0800

    net: mscc: ocelot: Fix use-after-free caused by cyclic delayed work
    
    [ Upstream commit bc9ea787079671cb19a8b25ff9f02be5ef6bfcf5 ]
    
    The origin code calls cancel_delayed_work() in ocelot_stats_deinit()
    to cancel the cyclic delayed work item ocelot->stats_work. However,
    cancel_delayed_work() may fail to cancel the work item if it is already
    executing. While destroy_workqueue() does wait for all pending work items
    in the work queue to complete before destroying the work queue, it cannot
    prevent the delayed work item from being rescheduled within the
    ocelot_check_stats_work() function. This limitation exists because the
    delayed work item is only enqueued into the work queue after its timer
    expires. Before the timer expiration, destroy_workqueue() has no visibility
    of this pending work item. Once the work queue appears empty,
    destroy_workqueue() proceeds with destruction. When the timer eventually
    expires, the delayed work item gets queued again, leading to the following
    warning:
    
    workqueue: cannot queue ocelot_check_stats_work on wq ocelot-switch-stats
    WARNING: CPU: 2 PID: 0 at kernel/workqueue.c:2255 __queue_work+0x875/0xaf0
    ...
    RIP: 0010:__queue_work+0x875/0xaf0
    ...
    RSP: 0018:ffff88806d108b10 EFLAGS: 00010086
    RAX: 0000000000000000 RBX: 0000000000000101 RCX: 0000000000000027
    RDX: 0000000000000027 RSI: 0000000000000004 RDI: ffff88806d123e88
    RBP: ffffffff813c3170 R08: 0000000000000000 R09: ffffed100da247d2
    R10: ffffed100da247d1 R11: ffff88806d123e8b R12: ffff88800c00f000
    R13: ffff88800d7285c0 R14: ffff88806d0a5580 R15: ffff88800d7285a0
    FS:  0000000000000000(0000) GS:ffff8880e5725000(0000) knlGS:0000000000000000
    CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
    CR2: 00007fe18e45ea10 CR3: 0000000005e6c000 CR4: 00000000000006f0
    Call Trace:
     <IRQ>
     ? kasan_report+0xc6/0xf0
     ? __pfx_delayed_work_timer_fn+0x10/0x10
     ? __pfx_delayed_work_timer_fn+0x10/0x10
     call_timer_fn+0x25/0x1c0
     __run_timer_base.part.0+0x3be/0x8c0
     ? __pfx_delayed_work_timer_fn+0x10/0x10
     ? rcu_sched_clock_irq+0xb06/0x27d0
     ? __pfx___run_timer_base.part.0+0x10/0x10
     ? try_to_wake_up+0xb15/0x1960
     ? _raw_spin_lock_irq+0x80/0xe0
     ? __pfx__raw_spin_lock_irq+0x10/0x10
     tmigr_handle_remote_up+0x603/0x7e0
     ? __pfx_tmigr_handle_remote_up+0x10/0x10
     ? sched_balance_trigger+0x1c0/0x9f0
     ? sched_tick+0x221/0x5a0
     ? _raw_spin_lock_irq+0x80/0xe0
     ? __pfx__raw_spin_lock_irq+0x10/0x10
     ? tick_nohz_handler+0x339/0x440
     ? __pfx_tmigr_handle_remote_up+0x10/0x10
     __walk_groups.isra.0+0x42/0x150
     tmigr_handle_remote+0x1f4/0x2e0
     ? __pfx_tmigr_handle_remote+0x10/0x10
     ? ktime_get+0x60/0x140
     ? lapic_next_event+0x11/0x20
     ? clockevents_program_event+0x1d4/0x2a0
     ? hrtimer_interrupt+0x322/0x780
     handle_softirqs+0x16a/0x550
     irq_exit_rcu+0xaf/0xe0
     sysvec_apic_timer_interrupt+0x70/0x80
     </IRQ>
    ...
    
    The following diagram reveals the cause of the above warning:
    
    CPU 0 (remove)             | CPU 1 (delayed work callback)
    mscc_ocelot_remove()       |
      ocelot_deinit()          | ocelot_check_stats_work()
        ocelot_stats_deinit()  |
          cancel_delayed_work()|   ...
                               |   queue_delayed_work()
          destroy_workqueue()  | (wait a time)
                               | __queue_work() //UAF
    
    The above scenario actually constitutes a UAF vulnerability.
    
    The ocelot_stats_deinit() is only invoked when initialization
    failure or resource destruction, so we must ensure that any
    delayed work items cannot be rescheduled.
    
    Replace cancel_delayed_work() with disable_delayed_work_sync()
    to guarantee proper cancellation of the delayed work item and
    ensure completion of any currently executing work before the
    workqueue is deallocated.
    
    A deadlock concern was considered: ocelot_stats_deinit() is called
    in a process context and is not holding any locks that the delayed
    work item might also need. Therefore, the use of the _sync() variant
    is safe here.
    
    This bug was identified through static analysis. To reproduce the
    issue and validate the fix, I simulated ocelot-switch device by
    writing a kernel module and prepared the necessary resources for
    the virtual ocelot-switch device's probe process. Then, removing
    the virtual device will trigger the mscc_ocelot_remove() function,
    which in turn destroys the workqueue.
    
    Fixes: a556c76adc05 ("net: mscc: Add initial Ocelot switch support")
    Signed-off-by: Duoming Zhou <duoming@zju.edu.cn>
    Link: https://patch.msgid.link/20251001011149.55073-1-duoming@zju.edu.cn
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 64dc47a13aa3d9daf7cec29b44dca8e22a6aea15
Author: Kuniyuki Iwashima <kuniyu@google.com>
Date:   Wed Oct 1 23:37:54 2025 +0000

    tcp: Don't call reqsk_fastopen_remove() in tcp_conn_request().
    
    [ Upstream commit 2e7cbbbe3d61c63606994b7ff73c72537afe2e1c ]
    
    syzbot reported the splat below in tcp_conn_request(). [0]
    
    If a listener is close()d while a TFO socket is being processed in
    tcp_conn_request(), inet_csk_reqsk_queue_add() does not set reqsk->sk
    and calls inet_child_forget(), which calls tcp_disconnect() for the
    TFO socket.
    
    After the cited commit, tcp_disconnect() calls reqsk_fastopen_remove(),
    where reqsk_put() is called due to !reqsk->sk.
    
    Then, reqsk_fastopen_remove() in tcp_conn_request() decrements the
    last req->rsk_refcnt and frees reqsk, and __reqsk_free() at the
    drop_and_free label causes the refcount underflow for the listener
    and double-free of the reqsk.
    
    Let's remove reqsk_fastopen_remove() in tcp_conn_request().
    
    Note that other callers make sure tp->fastopen_rsk is not NULL.
    
    [0]:
    refcount_t: underflow; use-after-free.
    WARNING: CPU: 12 PID: 5563 at lib/refcount.c:28 refcount_warn_saturate (lib/refcount.c:28)
    Modules linked in:
    CPU: 12 UID: 0 PID: 5563 Comm: syz-executor Not tainted syzkaller #0 PREEMPT(full)
    Hardware name: Google Google Compute Engine/Google Compute Engine, BIOS Google 07/12/2025
    RIP: 0010:refcount_warn_saturate (lib/refcount.c:28)
    Code: ab e8 8e b4 98 ff 0f 0b c3 cc cc cc cc cc 80 3d a4 e4 d6 01 00 75 9c c6 05 9b e4 d6 01 01 48 c7 c7 e8 df fb ab e8 6a b4 98 ff <0f> 0b e9 03 5b 76 00 cc 80 3d 7d e4 d6 01 00 0f 85 74 ff ff ff c6
    RSP: 0018:ffffa79fc0304a98 EFLAGS: 00010246
    RAX: d83af4db1c6b3900 RBX: ffff9f65c7a69020 RCX: d83af4db1c6b3900
    RDX: 0000000000000000 RSI: 00000000ffff7fff RDI: ffffffffac78a280
    RBP: 000000009d781b60 R08: 0000000000007fff R09: ffffffffac6ca280
    R10: 0000000000017ffd R11: 0000000000000004 R12: ffff9f65c7b4f100
    R13: ffff9f65c7d23c00 R14: ffff9f65c7d26000 R15: ffff9f65c7a64ef8
    FS:  00007f9f962176c0(0000) GS:ffff9f65fcf00000(0000) knlGS:0000000000000000
    CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
    CR2: 0000200000000180 CR3: 000000000dbbe006 CR4: 0000000000372ef0
    Call Trace:
     <IRQ>
     tcp_conn_request (./include/linux/refcount.h:400 ./include/linux/refcount.h:432 ./include/linux/refcount.h:450 ./include/net/sock.h:1965 ./include/net/request_sock.h:131 net/ipv4/tcp_input.c:7301)
     tcp_rcv_state_process (net/ipv4/tcp_input.c:6708)
     tcp_v6_do_rcv (net/ipv6/tcp_ipv6.c:1670)
     tcp_v6_rcv (net/ipv6/tcp_ipv6.c:1906)
     ip6_protocol_deliver_rcu (net/ipv6/ip6_input.c:438)
     ip6_input (net/ipv6/ip6_input.c:500)
     ipv6_rcv (net/ipv6/ip6_input.c:311)
     __netif_receive_skb (net/core/dev.c:6104)
     process_backlog (net/core/dev.c:6456)
     __napi_poll (net/core/dev.c:7506)
     net_rx_action (net/core/dev.c:7569 net/core/dev.c:7696)
     handle_softirqs (kernel/softirq.c:579)
     do_softirq (kernel/softirq.c:480)
     </IRQ>
    
    Fixes: 45c8a6cc2bcd ("tcp: Clear tcp_sk(sk)->fastopen_rsk in tcp_disconnect().")
    Reported-by: syzkaller <syzkaller@googlegroups.com>
    Signed-off-by: Kuniyuki Iwashima <kuniyu@google.com>
    Link: https://patch.msgid.link/20251001233755.1340927-1-kuniyu@google.com
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit badbd79313e6591616c1b78e29a9b71efed7f035
Author: Alexandr Sapozhnikov <alsp705@gmail.com>
Date:   Thu Oct 2 12:14:47 2025 +0300

    net/sctp: fix a null dereference in sctp_disposition sctp_sf_do_5_1D_ce()
    
    [ Upstream commit 2f3119686ef50319490ccaec81a575973da98815 ]
    
    If new_asoc->peer.adaptation_ind=0 and sctp_ulpevent_make_authkey=0
    and sctp_ulpevent_make_authkey() returns 0, then the variable
    ai_ev remains zero and the zero will be dereferenced
    in the sctp_ulpevent_free() function.
    
    Signed-off-by: Alexandr Sapozhnikov <alsp705@gmail.com>
    Acked-by: Xin Long <lucien.xin@gmail.com>
    Fixes: 30f6ebf65bc4 ("sctp: add SCTP_AUTH_NO_AUTH type for AUTHENTICATION_EVENT")
    Link: https://patch.msgid.link/20251002091448.11-1-alsp705@gmail.com
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 9895f936f83d1d5167a47fcc0d9ea40bffde2094
Author: Ian Forbes <ian.forbes@broadcom.com>
Date:   Fri Sep 26 14:54:26 2025 -0500

    drm/vmwgfx: Fix copy-paste typo in validation
    
    [ Upstream commit 228c5d44dffe8c293cd2d2f0e7ea45e64565b1c4 ]
    
    'entry' should be 'val' which is the loop iterator.
    
    Fixes: 9e931f2e0970 ("drm/vmwgfx: Refactor resource validation hashtable to use linux/hashtable implementation.")
    Signed-off-by: Ian Forbes <ian.forbes@broadcom.com>
    Reviewed-by: Zack Rusin <zack.rusin@broadcom.com>
    Signed-off-by: Zack Rusin <zack.rusin@broadcom.com>
    Link: https://lore.kernel.org/r/20250926195427.1405237-2-ian.forbes@broadcom.com
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 65608e991c2d771c13404e5c7ae122ac3c3357a4
Author: Ian Forbes <ian.forbes@broadcom.com>
Date:   Fri Sep 26 14:54:25 2025 -0500

    drm/vmwgfx: Fix Use-after-free in validation
    
    [ Upstream commit dfe1323ab3c8a4dd5625ebfdba44dc47df84512a ]
    
    Nodes stored in the validation duplicates hashtable come from an arena
    allocator that is cleared at the end of vmw_execbuf_process. All nodes
    are expected to be cleared in vmw_validation_drop_ht but this node escaped
    because its resource was destroyed prematurely.
    
    Fixes: 64ad2abfe9a6 ("drm/vmwgfx: Adapt validation code for reference-free lookups")
    Reported-by: Kuzey Arda Bulut <kuzeyardabulut@gmail.com>
    Signed-off-by: Ian Forbes <ian.forbes@broadcom.com>
    Reviewed-by: Zack Rusin <zack.rusin@broadcom.com>
    Signed-off-by: Zack Rusin <zack.rusin@broadcom.com>
    Link: https://lore.kernel.org/r/20250926195427.1405237-1-ian.forbes@broadcom.com
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit b6fca0a07989f361ceda27cb2d09c555d4d4a964
Author: Zack Rusin <zack.rusin@broadcom.com>
Date:   Wed Sep 17 11:36:55 2025 -0400

    drm/vmwgfx: Fix a null-ptr access in the cursor snooper
    
    [ Upstream commit 5ac2c0279053a2c5265d46903432fb26ae2d0da2 ]
    
    Check that the resource which is converted to a surface exists before
    trying to use the cursor snooper on it.
    
    vmw_cmd_res_check allows explicit invalid (SVGA3D_INVALID_ID) identifiers
    because some svga commands accept SVGA3D_INVALID_ID to mean "no surface",
    unfortunately functions that accept the actual surfaces as objects might
    (and in case of the cursor snooper, do not) be able to handle null
    objects. Make sure that we validate not only the identifier (via the
    vmw_cmd_res_check) but also check that the actual resource exists before
    trying to do something with it.
    
    Fixes unchecked null-ptr reference in the snooping code.
    
    Signed-off-by: Zack Rusin <zack.rusin@broadcom.com>
    Fixes: c0951b797e7d ("drm/vmwgfx: Refactor resource management")
    Reported-by: Kuzey Arda Bulut <kuzeyardabulut@gmail.com>
    Cc: Broadcom internal kernel review list <bcm-kernel-feedback-list@broadcom.com>
    Cc: dri-devel@lists.freedesktop.org
    Reviewed-by: Ian Forbes <ian.forbes@broadcom.com>
    Link: https://lore.kernel.org/r/20250917153655.1968583-1-zack.rusin@broadcom.com
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 37c21157fd102a0b75eeeb55ad2eaa6d0e05b70d
Author: Vineeth Vijayan <vneethv@linux.ibm.com>
Date:   Wed Oct 1 15:38:17 2025 +0200

    s390/cio: Update purge function to unregister the unused subchannels
    
    [ Upstream commit 9daa5a8795865f9a3c93d8d1066785b07ded6073 ]
    
    Starting with 'commit 2297791c92d0 ("s390/cio: dont unregister
    subchannel from child-drivers")', cio no longer unregisters
    subchannels when the attached device is invalid or unavailable.
    
    As an unintended side-effect, the cio_ignore purge function no longer
    removes subchannels for devices on the cio_ignore list if no CCW device
    is attached. This situation occurs when a CCW device is non-operational
    or unavailable
    
    To ensure the same outcome of the purge function as when the
    current cio_ignore list had been active during boot, update the purge
    function to remove I/O subchannels without working CCW devices if the
    associated device number is found on the cio_ignore list.
    
    Fixes: 2297791c92d0 ("s390/cio: dont unregister subchannel from child-drivers")
    Suggested-by: Peter Oberparleiter <oberpar@linux.ibm.com>
    Reviewed-by: Peter Oberparleiter <oberpar@linux.ibm.com>
    Signed-off-by: Vineeth Vijayan <vneethv@linux.ibm.com>
    Signed-off-by: Heiko Carstens <hca@linux.ibm.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 71f3f74628fab92990446ad2372c3e1bb8b50e10
Author: Raag Jadav <raag.jadav@intel.com>
Date:   Thu Sep 18 16:02:00 2025 +0530

    drm/xe/i2c: Don't rely on d3cold.allowed flag in system PM path
    
    [ Upstream commit 1af59cd5cc2b65d7fc95165f056695ce3f171133 ]
    
    In S3 and above sleep states, the device can loose power regardless of
    d3cold.allowed flag. Bring up I2C controller explicitly in system PM
    path to ensure its normal operation after losing power.
    
    v2: Cover S3 and above states (Rodrigo)
    
    Fixes: 0ea07b69517a ("drm/xe/pm: Wire up suspend/resume for I2C controller")
    Signed-off-by: Raag Jadav <raag.jadav@intel.com>
    Reviewed-by: Rodrigo Vivi <rodrigo.vivi@intel.com>
    Link: https://lore.kernel.org/r/20250918103200.2952576-1-raag.jadav@intel.com
    Signed-off-by: Rodrigo Vivi <rodrigo.vivi@intel.com>
    (cherry picked from commit e4863f1159befcd70df24fcb5458afaf2feab043)
    Signed-off-by: Lucas De Marchi <lucas.demarchi@intel.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 10e38805797b2236c332982dd703071a408b1f3c
Author: Shuicheng Lin <shuicheng.lin@intel.com>
Date:   Thu Sep 25 02:31:46 2025 +0000

    drm/xe/hw_engine_group: Fix double write lock release in error path
    
    [ Upstream commit 08fdfd260e641da203f80aff8d3ed19c5ecceb7d ]
    
    In xe_hw_engine_group_get_mode(), a write lock is acquired before
    calling switch_mode(), which in turn invokes
    xe_hw_engine_group_suspend_faulting_lr_jobs().
    
    On failure inside xe_hw_engine_group_suspend_faulting_lr_jobs(),
    the write lock is released there, and then again in
    xe_hw_engine_group_get_mode(), leading to a double release.
    
    Fix this by keeping both acquire and release operation in
    xe_hw_engine_group_get_mode().
    
    Fixes: 770bd1d34113 ("drm/xe/hw_engine_group: Ensure safe transition between execution modes")
    Cc: Francois Dugast <francois.dugast@intel.com>
    Signed-off-by: Shuicheng Lin <shuicheng.lin@intel.com>
    Reviewed-by: Francois Dugast <francois.dugast@intel.com>
    Link: https://lore.kernel.org/r/20250925023145.1203004-2-shuicheng.lin@intel.com
    Signed-off-by: Lucas De Marchi <lucas.demarchi@intel.com>
    (cherry picked from commit 662d98b8b373007fa1b08ba93fee11f6fd3e387c)
    Signed-off-by: Lucas De Marchi <lucas.demarchi@intel.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit b48179caeb6eebd70f57c879f0e035b3cdf52189
Author: Dan Carpenter <dan.carpenter@linaro.org>
Date:   Tue Sep 30 15:25:01 2025 +0300

    net/mlx4: prevent potential use after free in mlx4_en_do_uc_filter()
    
    [ Upstream commit 4f0d91ba72811fd5dd577bcdccd7fed649aae62c ]
    
    Print "entry->mac" before freeing "entry".  The "entry" pointer is
    freed with kfree_rcu() so it's unlikely that we would trigger this
    in real life, but it's safer to re-order it.
    
    Fixes: cc5387f7346a ("net/mlx4_en: Add unicast MAC filtering")
    Signed-off-by: Dan Carpenter <dan.carpenter@linaro.org>
    Reviewed-by: Tariq Toukan <tariqt@nvidia.com>
    Link: https://patch.msgid.link/aNvMHX4g8RksFFvV@stanley.mountain
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit a72a7c4f675080a324d4c2167bd2314d968279f1
Author: Bhanu Seshu Kumar Valluri <bhanuseshukumar@gmail.com>
Date:   Tue Sep 30 14:19:02 2025 +0530

    net: usb: lan78xx: Fix lost EEPROM read timeout error(-ETIMEDOUT) in lan78xx_read_raw_eeprom
    
    [ Upstream commit 49bdb63ff64469a6de8ea901aef123c75be9bbe7 ]
    
    Syzbot reported read of uninitialized variable BUG with following call stack.
    
    lan78xx 8-1:1.0 (unnamed net_device) (uninitialized): EEPROM read operation timeout
    =====================================================
    BUG: KMSAN: uninit-value in lan78xx_read_eeprom drivers/net/usb/lan78xx.c:1095 [inline]
    BUG: KMSAN: uninit-value in lan78xx_init_mac_address drivers/net/usb/lan78xx.c:1937 [inline]
    BUG: KMSAN: uninit-value in lan78xx_reset+0x999/0x2cd0 drivers/net/usb/lan78xx.c:3241
     lan78xx_read_eeprom drivers/net/usb/lan78xx.c:1095 [inline]
     lan78xx_init_mac_address drivers/net/usb/lan78xx.c:1937 [inline]
     lan78xx_reset+0x999/0x2cd0 drivers/net/usb/lan78xx.c:3241
     lan78xx_bind+0x711/0x1690 drivers/net/usb/lan78xx.c:3766
     lan78xx_probe+0x225c/0x3310 drivers/net/usb/lan78xx.c:4707
    
    Local variable sig.i.i created at:
     lan78xx_read_eeprom drivers/net/usb/lan78xx.c:1092 [inline]
     lan78xx_init_mac_address drivers/net/usb/lan78xx.c:1937 [inline]
     lan78xx_reset+0x77e/0x2cd0 drivers/net/usb/lan78xx.c:3241
     lan78xx_bind+0x711/0x1690 drivers/net/usb/lan78xx.c:3766
    
    The function lan78xx_read_raw_eeprom failed to properly propagate EEPROM
    read timeout errors (-ETIMEDOUT). In the fallthrough path, it first
    attempted to restore the pin configuration for LED outputs and then
    returned only the status of that restore operation, discarding the
    original timeout error.
    
    As a result, callers could mistakenly treat the data buffer as valid
    even though the EEPROM read had actually timed out with no data or partial
    data.
    
    To fix this, handle errors in restoring the LED pin configuration separately.
    If the restore succeeds, return any prior EEPROM timeout error correctly
    to the caller.
    
    Reported-by: syzbot+62ec8226f01cb4ca19d9@syzkaller.appspotmail.com
    Closes: https://syzkaller.appspot.com/bug?extid=62ec8226f01cb4ca19d9
    Fixes: 8b1b2ca83b20 ("net: usb: lan78xx: Improve error handling in EEPROM and OTP operations")
    Signed-off-by: Bhanu Seshu Kumar Valluri <bhanuseshukumar@gmail.com>
    Reviewed-by: Oleksij Rempel <o.rempel@pengutronix.de>
    Link: https://patch.msgid.link/20250930084902.19062-1-bhanuseshukumar@gmail.com
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit e298bf6f5579feda1044cc4f1ee842b135e9b422
Author: Peter Ujfalusi <peter.ujfalusi@linux.intel.com>
Date:   Thu Oct 2 10:47:19 2025 +0300

    ASoC: SOF: Intel: Read the LLP via the associated Link DMA channel
    
    [ Upstream commit aaab61de1f1e44a2ab527e935474e2e03a0f6b08 ]
    
    It is allowed to mix Link and Host DMA channels in a way that their index
    is different. In this case we would read the LLP from a channel which is
    not used or used for other operation.
    
    Such case can be reproduced on cAVS2.5 or ACE1 platforms with soundwire
    configuration:
    playback to SDW would take Host channel 0 (stream_tag 1) and no Link DMA
    used
    Second playback to HDMI (HDA) would use Host channel 1 (stream_tag 2) and
    Link channel 0 (stream_tag 1).
    
    In this case reading the LLP from channel 2 is incorrect as that is not the
    Link channel used for the HDMI playback.
    
    To correct this, we should look up the BE and get the channel used on the
    Link side.
    
    Fixes: 67b182bea08a ("ASoC: SOF: Intel: hda: Implement get_stream_position (Linear Link Position)")
    Signed-off-by: Peter Ujfalusi <peter.ujfalusi@linux.intel.com>
    Reviewed-by: Kai Vehmanen <kai.vehmanen@linux.intel.com>
    Reviewed-by: Ranjani Sridharan <ranjani.sridharan@linux.intel.com>
    Link: https://patch.msgid.link/20251002074719.2084-6-peter.ujfalusi@linux.intel.com
    Signed-off-by: Mark Brown <broonie@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 2ffb976c2d1fbebce5562b5b675b6702456fdacf
Author: Huacai Chen <chenhuacai@kernel.org>
Date:   Thu Oct 2 22:38:57 2025 +0800

    LoongArch: Init acpi_gbl_use_global_lock to false
    
    [ Upstream commit 98662be7ef20d2b88b598f72e7ce9b6ac26a40f9 ]
    
    Init acpi_gbl_use_global_lock to false, in order to void error messages
    during boot phase:
    
     ACPI Error: Could not enable GlobalLock event (20240827/evxfevnt-182)
     ACPI Error: No response from Global Lock hardware, disabling lock (20240827/evglock-59)
    
    Fixes: 628c3bb40e9a8cefc0a6 ("LoongArch: Add boot and setup routines")
    Signed-off-by: Huacai Chen <chenhuacai@loongson.cn>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 396413586eaeeddfd0fbc60ea8c0f973733a0b4d
Author: Huacai Chen <chenhuacai@kernel.org>
Date:   Thu Oct 2 22:38:57 2025 +0800

    LoongArch: Fix build error for LTO with LLVM-18
    
    [ Upstream commit 19baac378a5f4c34e61007023cfcb605cc64c76d ]
    
    Commit b15212824a01 ("LoongArch: Make LTO case independent in Makefile")
    moves "KBUILD_LDFLAGS += -mllvm --loongarch-annotate-tablejump" out of
    CONFIG_CC_HAS_ANNOTATE_TABLEJUMP, which breaks the build for LLVM-18, as
    '--loongarch-annotate-tablejump' is unimplemented there:
    
    ld.lld: error: -mllvm: ld.lld: Unknown command line argument '--loongarch-annotate-tablejump'.
    
    Call ld-option to detect '--loongarch-annotate-tablejump' before use, so
    as to fix the build error.
    
    Fixes: b15212824a01 ("LoongArch: Make LTO case independent in Makefile")
    Reported-by: Nathan Chancellor <nathan@kernel.org>
    Reviewed-by: Nathan Chancellor <nathan@kernel.org>
    Tested-by: Nathan Chancellor <nathan@kernel.org> # build
    Suggested-by: WANG Rui <wangrui@loongson.cn>
    Signed-off-by: Huacai Chen <chenhuacai@loongson.cn>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 2e0f153918429860547fe6064a447a76f3936b7a
Author: Tiezhu Yang <yangtiezhu@loongson.cn>
Date:   Thu Oct 2 22:38:57 2025 +0800

    LoongArch: Add cflag -fno-isolate-erroneous-paths-dereference
    
    [ Upstream commit abb2a5572264b425e6dd9c213b735a82ab0ca68a ]
    
    Currently, when compiling with GCC, there is no "break 7" instruction
    for zero division due to using the option -mno-check-zero-division, but
    the compiler still generates "break 0" instruction for zero division.
    
    Here is a simple example:
    
      $ cat test.c
      int div(int a)
      {
              return a / 0;
      }
      $ gcc -O2 -S test.c -o test.s
    
    GCC generates "break 0" on LoongArch and "ud2" on x86, objtool decodes
    "ud2" as INSN_BUG for x86, so decode "break 0" as INSN_BUG can fix the
    objtool warnings for LoongArch, but this is not the intention.
    
    When decoding "break 0" as INSN_TRAP in the previous commit, the aim is
    to handle "break 0" as a trap. The generated "break 0" for zero division
    by GCC is not proper, it should generate a break instruction with proper
    bug type, so add the GCC option -fno-isolate-erroneous-paths-dereference
    to avoid generating the unexpected "break 0" instruction for now.
    
    Reported-by: kernel test robot <lkp@intel.com>
    Closes: https://lore.kernel.org/r/202509200413.7uihAxJ5-lkp@intel.com/
    Fixes: baad7830ee9a ("objtool/LoongArch: Mark types based on break immediate code")
    Suggested-by: WANG Rui <wangrui@loongson.cn>
    Signed-off-by: Tiezhu Yang <yangtiezhu@loongson.cn>
    Signed-off-by: Huacai Chen <chenhuacai@loongson.cn>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 4a6261c2fd02147d6bf773ecab481392a432c3b2
Author: Peter Ujfalusi <peter.ujfalusi@linux.intel.com>
Date:   Thu Oct 2 16:57:52 2025 +0300

    ASoC: SOF: Intel: hda-pcm: Place the constraint on period time instead of buffer time
    
    [ Upstream commit 45ad27d9a6f7c620d8bbc80be3bab1faf37dfa0a ]
    
    Instead of constraining the ALSA buffer time to be double of the firmware
    host buffer size, it is better to set it for the period time.
    This will implicitly constrain the buffer time to a safe value
    (num_periods is at least 2) and prohibits applications to set smaller
    period size than what will be covered by the initial DMA burst.
    
    Fixes: fe76d2e75a6d ("ASoC: SOF: Intel: hda-pcm: Use dsp_max_burst_size_in_ms to place constraint")
    Signed-off-by: Peter Ujfalusi <peter.ujfalusi@linux.intel.com>
    Reviewed-by: Ranjani Sridharan <ranjani.sridharan@linux.intel.com>
    Reviewed-by: Kai Vehmanen <kai.vehmanen@linux.intel.com>
    Reviewed-by: Bard Liao <yung-chuan.liao@linux.intel.com>
    Link: https://patch.msgid.link/20251002135752.2430-4-peter.ujfalusi@linux.intel.com
    Signed-off-by: Mark Brown <broonie@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit a067ebf116804f31b6a7c9a34685f1ce0b865866
Author: Peter Ujfalusi <peter.ujfalusi@linux.intel.com>
Date:   Thu Oct 2 16:57:51 2025 +0300

    ASoC: SOF: ipc4-topology: Account for different ChainDMA host buffer size
    
    [ Upstream commit 3dcf683bf1062d69014fe81b90d285c7eb85ca8a ]
    
    For ChainDMA the firmware allocates 5ms host buffer instead of the standard
    4ms which should be taken into account when setting the constraint on the
    buffer size.
    
    Fixes: 842bb8b62cc6 ("ASoC: SOF: ipc4-topology: Save the DMA maximum burst size for PCMs")
    Signed-off-by: Peter Ujfalusi <peter.ujfalusi@linux.intel.com>
    Reviewed-by: Ranjani Sridharan <ranjani.sridharan@linux.intel.com>
    Reviewed-by: Kai Vehmanen <kai.vehmanen@linux.intel.com>
    Reviewed-by: Bard Liao <yung-chuan.liao@linux.intel.com>
    Link: https://patch.msgid.link/20251002135752.2430-3-peter.ujfalusi@linux.intel.com
    Signed-off-by: Mark Brown <broonie@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 5024aadb69bc8191a0e502f6196287b23ed844c2
Author: Peter Ujfalusi <peter.ujfalusi@linux.intel.com>
Date:   Thu Oct 2 16:57:50 2025 +0300

    ASoC: SOF: ipc4-topology: Correct the minimum host DMA buffer size
    
    [ Upstream commit a7fe5ff832d61d9393095bc3dd5f06f4af7da3c1 ]
    
    The firmware has changed the minimum host buffer size from 2 periods to
    4 periods (1 period is 1ms) which was missed by the kernel side.
    
    Adjust the SOF_IPC4_MIN_DMA_BUFFER_SIZE to 4 ms to align with firmware.
    
    Link: https://github.com/thesofproject/sof/commit/f0a14a3f410735db18a79eb7a5f40dc49fdee7a7
    Fixes: 594c1bb9ff73 ("ASoC: SOF: ipc4-topology: Do not parse the DMA_BUFFER_SIZE token")
    Signed-off-by: Peter Ujfalusi <peter.ujfalusi@linux.intel.com>
    Reviewed-by: Ranjani Sridharan <ranjani.sridharan@linux.intel.com>
    Reviewed-by: Kai Vehmanen <kai.vehmanen@linux.intel.com>
    Reviewed-by: Bard Liao <yung-chuan.liao@linux.intel.com>
    Link: https://patch.msgid.link/20251002135752.2430-2-peter.ujfalusi@linux.intel.com
    Signed-off-by: Mark Brown <broonie@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 11392a9ed0617acac955f7084259ff4aa39cd9d7
Author: Ian Rogers <irogers@google.com>
Date:   Wed Oct 1 11:12:28 2025 -0700

    perf bpf_counter: Fix handling of cpumap fixing hybrid
    
    [ Upstream commit b91917c0c6fa6df97ec0222d8d6285ab2d60c21b ]
    
    Don't open evsels on all CPUs, open them just on the CPUs they
    support. This avoids opening say an e-core event on a p-core and
    getting a failure - achieve this by getting rid of the "all_cpu_map".
    
    In install_pe functions don't use the cpu_map_idx as a CPU number,
    translate the cpu_map_idx, which is a dense index into the cpu_map
    skipping holes at the beginning, to a proper CPU number.
    
    Before:
    ```
    $ perf stat --bpf-counters -a -e cycles,instructions -- sleep 1
    
     Performance counter stats for 'system wide':
    
       <not supported>      cpu_atom/cycles/
           566,270,672      cpu_core/cycles/
       <not supported>      cpu_atom/instructions/
           572,792,836      cpu_core/instructions/           #    1.01  insn per cycle
    
           1.001595384 seconds time elapsed
    ```
    
    After:
    ```
    $ perf stat --bpf-counters -a -e cycles,instructions -- sleep 1
    
     Performance counter stats for 'system wide':
    
           443,299,201      cpu_atom/cycles/
         1,233,919,737      cpu_core/cycles/
           213,634,112      cpu_atom/instructions/           #    0.48  insn per cycle
         2,758,965,527      cpu_core/instructions/           #    2.24  insn per cycle
    
           1.001699485 seconds time elapsed
    ```
    
    Fixes: 7fac83aaf2eecc9e ("perf stat: Introduce 'bperf' to share hardware PMCs with BPF")
    Signed-off-by: Ian Rogers <irogers@google.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Athira Rajeev <atrajeev@linux.vnet.ibm.com>
    Cc: bpf@vger.kernel.org
    Cc: Gabriele Monaco <gmonaco@redhat.com>
    Cc: Howard Chu <howardchu95@gmail.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: James Clark <james.clark@linaro.org>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Cc: Song Liu <songliubraving@fb.com>
    Cc: Tengda Wu <wutengda@huaweicloud.com>
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit e4550cdec9816dcf5885b9c3ca94db6780db1ed2
Author: Sean Christopherson <seanjc@google.com>
Date:   Wed Aug 27 17:01:50 2025 -0700

    mshv: Handle NEED_RESCHED_LAZY before transferring to guest
    
    [ Upstream commit 0ebac01a00be972020c002a7fe0bb6b6fca8410f ]
    
    Check for NEED_RESCHED_LAZY, not just NEED_RESCHED, prior to transferring
    control to a guest.  Failure to check for lazy resched can unnecessarily
    delay rescheduling until the next tick when using a lazy preemption model.
    
    Note, ideally both the checking and processing of TIF bits would be handled
    in common code, to avoid having to keep three separate paths synchronized,
    but defer such cleanups to the future to keep the fix as standalone as
    possible.
    
    Cc: Nuno Das Neves <nunodasneves@linux.microsoft.com>
    Cc: Mukesh R <mrathor@linux.microsoft.com>
    Fixes: 621191d709b1 ("Drivers: hv: Introduce mshv_root module to expose /dev/mshv to VMMs")
    Signed-off-by: Sean Christopherson <seanjc@google.com>
    Tested-by: Nuno Das Neves <nunodasneves@linux.microsoft.com>
    Reviewed-by: Nuno Das Neves <nunodasneves@linux.microsoft.com>
    Signed-off-by: Wei Liu <wei.liu@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 6fa2a8073d6101577d2d47072ee4c7856045e0eb
Author: Daniel Lee <chullee@google.com>
Date:   Mon Sep 29 18:09:39 2025 -0700

    scsi: ufs: sysfs: Make HID attributes visible
    
    [ Upstream commit bb7663dec67b691528f104894429b3859fb16c14 ]
    
    Call sysfs_update_group() after reading the device descriptor to ensure
    the HID sysfs attributes are visible when the feature is supported.
    
    Fixes: ae7795a8c258 ("scsi: ufs: core: Add HID support")
    Signed-off-by: Daniel Lee <chullee@google.com>
    Reviewed-by: Bart Van Assche <bvanassche@acm.org>
    Signed-off-by: Martin K. Petersen <martin.petersen@oracle.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit d994092013c7f4f6c0a4a90c9a0eea70ac6b31a2
Author: Ian Rogers <irogers@google.com>
Date:   Fri Aug 29 22:35:49 2025 -0700

    perf bpf-filter: Fix opts declaration on older libbpfs
    
    [ Upstream commit 3a0f56d72a7575f03187a85b7869c76a862b40ab ]
    
    Building perf with LIBBPF_DYNAMIC (ie not the default static linking of
    libbpf with perf) is breaking as the libbpf isn't version 1.7 or newer,
    where dont_enable is added to bpf_perf_event_opts.
    
    To avoid this breakage add a compile time version check and don't
    declare the variable when not present.
    
    Fixes: 5e2ac8e8571df54d ("perf bpf-filter: Enable events manually")
    Signed-off-by: Ian Rogers <irogers@google.com>
    Tested-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Alexei Starovoitov <ast@kernel.org>
    Cc: bpf@vger.kernel.org
    Cc: Hao Ge <gehao@kylinos.cn>
    Cc: Ilya Leoshkevich <iii@linux.ibm.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Cc: Thomas Richter <tmricht@linux.ibm.com>
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit feb946d2fc9dc754bf3d594d42cd228860ff8647
Author: Duoming Zhou <duoming@zju.edu.cn>
Date:   Sat Sep 20 21:42:01 2025 +0800

    scsi: mvsas: Fix use-after-free bugs in mvs_work_queue
    
    [ Upstream commit 60cd16a3b7439ccb699d0bf533799eeb894fd217 ]
    
    During the detaching of Marvell's SAS/SATA controller, the original code
    calls cancel_delayed_work() in mvs_free() to cancel the delayed work
    item mwq->work_q. However, if mwq->work_q is already running, the
    cancel_delayed_work() may fail to cancel it. This can lead to
    use-after-free scenarios where mvs_free() frees the mvs_info while
    mvs_work_queue() is still executing and attempts to access the
    already-freed mvs_info.
    
    A typical race condition is illustrated below:
    
    CPU 0 (remove)            | CPU 1 (delayed work callback)
    mvs_pci_remove()          |
      mvs_free()              | mvs_work_queue()
        cancel_delayed_work() |
          kfree(mvi)          |
                              |   mvi-> // UAF
    
    Replace cancel_delayed_work() with cancel_delayed_work_sync() to ensure
    that the delayed work item is properly canceled and any executing
    delayed work item completes before the mvs_info is deallocated.
    
    This bug was found by static analysis.
    
    Fixes: 20b09c2992fe ("[SCSI] mvsas: add support for 94xx; layout change; bug fixes")
    Signed-off-by: Duoming Zhou <duoming@zju.edu.cn>
    Signed-off-by: Martin K. Petersen <martin.petersen@oracle.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit eb639aac99ea6c5c8ed4e6b20ab24145b09c4768
Author: Aaron Kling <webgeek1234@gmail.com>
Date:   Thu Aug 28 21:48:12 2025 -0500

    cpufreq: tegra186: Set target frequency for all cpus in policy
    
    [ Upstream commit 0b1bb980fd7cae126ee3d59f817068a13e321b07 ]
    
    The original commit set all cores in a cluster to a shared policy, but
    did not update set_target to apply a frequency change to all cores for
    the policy. This caused most cores to remain stuck at their boot
    frequency.
    
    Fixes: be4ae8c19492 ("cpufreq: tegra186: Share policy per cluster")
    Signed-off-by: Aaron Kling <webgeek1234@gmail.com>
    Reviewed-by: Mikko Perttunen <mperttunen@nvidia.com>
    Signed-off-by: Viresh Kumar <viresh.kumar@linaro.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 7b0778d11ed52b6299fc3ba7de0bf5cfe857ce9c
Author: Pin-yen Lin <treapking@chromium.org>
Date:   Fri Sep 26 18:23:18 2025 +0800

    PM: sleep: Do not wait on SYNC_STATE_ONLY device links
    
    [ Upstream commit 632d31067be2f414c57955efcf29c79290cc749b ]
    
    Device links with DL_FLAG_SYNC_STATE_ONLY should not affect system
    suspend and resume, and functions like device_reorder_to_tail() and
    device_link_add() don't try to reorder the consumers with that flag.
    
    However, dpm_wait_for_consumers() and dpm_wait_for_suppliers() don't
    check thas flag before triggering dpm_wait(), leading to potential hang
    during suspend/resume.
    
    This can be reproduced on MT8186 Corsola Chromebook with devicetree like:
    
    usb-a-connector {
            compatible = "usb-a-connector";
            port {
                    usb_a_con: endpoint {
                            remote-endpoint = <&usb_hs>;
                    };
            };
    };
    
    usb_host {
            compatible = "mediatek,mt8186-xhci", "mediatek,mtk-xhci";
            port {
                    usb_hs: endpoint {
                            remote-endpoint = <&usb_a_con>;
                    };
            };
    };
    
    In this case, the two nodes form a cycle and a SYNC_STATE_ONLY devlink
    between usb_host (supplier) and usb-a-connector (consumer) is created.
    
    Address this by exporting device_link_flag_is_sync_state_only() and
    making dpm_wait_for_consumers() and dpm_wait_for_suppliers() use it
    when deciding if dpm_wait() should be called.
    
    Fixes: 05ef983e0d65a ("driver core: Add device link support for SYNC_STATE_ONLY flag")
    Signed-off-by: Pin-yen Lin <treapking@chromium.org>
    Link: https://patch.msgid.link/20250926102320.4053167-1-treapking@chromium.org
    [ rjw: Subject and changelog edits ]
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 0790fd9c77529d64af26067c674e64bab96bc8bc
Author: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Date:   Tue Sep 2 15:45:14 2025 +0200

    PM: core: Add two macros for walking device links
    
    [ Upstream commit 3ce3f569991347d2085925041f4932232da43bcf ]
    
    Add separate macros for walking links to suppliers and consumers of a
    device to help device links users to avoid exposing the internals of
    struct dev_links_info in their code and possible coding mistakes related
    to that.
    
    Accordingly, use the new macros to replace open-coded device links list
    walks in the core power management code.
    
    No intentional functional impact.
    
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Reviewed-by: Ulf Hansson <ulf.hansson@linaro.org>
    Acked-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
    Link: https://patch.msgid.link/1944671.tdWV9SEqCh@rafael.j.wysocki
    Stable-dep-of: 632d31067be2 ("PM: sleep: Do not wait on SYNC_STATE_ONLY device links")
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 10829bb8373cba2e87ea64315eaa7f12a6279f03
Author: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Date:   Tue Sep 2 15:43:50 2025 +0200

    PM: core: Annotate loops walking device links as _srcu
    
    [ Upstream commit fdd9ae23bb989fa9ed1beebba7d3e0c82c7c81ae ]
    
    Since SRCU is used for the protection of device link lists, the loops
    over device link lists in multiple places in drivers/base/power/main.c
    and in pm_runtime_get_suppliers() should be annotated as _srcu rather
    than as _rcu which is the case currently.
    
    Change the annotations accordingly.
    
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Reviewed-by: Ulf Hansson <ulf.hansson@linaro.org>
    Acked-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
    Link: https://patch.msgid.link/2393512.ElGaqSPkdT@rafael.j.wysocki
    Stable-dep-of: 632d31067be2 ("PM: sleep: Do not wait on SYNC_STATE_ONLY device links")
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 583cc76347a87a6a7663dfc55715d4928524c2b8
Author: Feng Yang <yangfeng@kylinos.cn>
Date:   Thu Sep 25 10:08:22 2025 +0800

    tracing: Fix the bug where bpf_get_stackid returns -EFAULT on the ARM64
    
    [ Upstream commit fd2f74f8f3d3c1a524637caf5bead9757fae4332 ]
    
    When using bpf_program__attach_kprobe_multi_opts on ARM64 to hook a BPF program
    that contains the bpf_get_stackid function, the BPF program fails
    to obtain the stack trace and returns -EFAULT.
    
    This is because ftrace_partial_regs omits the configuration of the pstate register,
    leaving pstate at the default value of 0. When get_perf_callchain executes,
    it uses user_mode(regs) to determine whether it is in kernel mode.
    This leads to a misjudgment that the code is in user mode,
    so perf_callchain_kernel is not executed and the function returns directly.
    As a result, trace->nr becomes 0, and finally -EFAULT is returned.
    
    Therefore, the assignment of the pstate register is added here.
    
    Fixes: b9b55c8912ce ("tracing: Add ftrace_partial_regs() for converting ftrace_regs to pt_regs")
    Closes: https://lore.kernel.org/bpf/20250919071902.554223-1-yangfeng59949@163.com/
    Signed-off-by: Feng Yang <yangfeng@kylinos.cn>
    Tested-by: Jiri Olsa <jolsa@kernel.org>
    Acked-by: Masami Hiramatsu (Google) <mhiramat@kernel.org>
    Signed-off-by: Will Deacon <will@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 46d127d619a3720694e4144d961601c3b67a2033
Author: Jeff Layton <jlayton@kernel.org>
Date:   Wed Jul 30 09:24:36 2025 -0400

    nfsd: fix timestamp updates in CB_GETATTR
    
    [ Upstream commit b40b1ba37ad5b6099c426765c4bc327c08b390b9 ]
    
    When updating the local timestamps from CB_GETATTR, the updated values
    are not being properly vetted.
    
    Compare the update times vs. the saved times in the delegation rather
    than the current times in the inode. Also, ensure that the ctime is
    properly vetted vs. its original value.
    
    Fixes: 6ae30d6eb26b ("nfsd: add support for delegated timestamps")
    Signed-off-by: Jeff Layton <jlayton@kernel.org>
    Signed-off-by: Chuck Lever <chuck.lever@oracle.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 19fdcfec3ac143d2e4efb635982a7268d094345b
Author: Jeff Layton <jlayton@kernel.org>
Date:   Wed Jul 30 09:24:35 2025 -0400

    nfsd: fix SETATTR updates for delegated timestamps
    
    [ Upstream commit 3952f1cbcbc454b2cb639ddbf165c07068e90371 ]
    
    SETATTRs containing delegated timestamp updates are currently not being
    vetted properly. Since we no longer need to compare the timestamps vs.
    the current timestamps, move the vetting of delegated timestamps wholly
    into nfsd.
    
    Rename the set_cb_time() helper to nfsd4_vet_deleg_time(), and make it
    non-static. Add a new vet_deleg_attrs() helper that is called from
    nfsd4_setattr that uses nfsd4_vet_deleg_time() to properly validate the
    all the timestamps. If the validation indicates that the update should
    be skipped, unset the appropriate flags in ia_valid.
    
    Fixes: 7e13f4f8d27d ("nfsd: handle delegated timestamps in SETATTR")
    Signed-off-by: Jeff Layton <jlayton@kernel.org>
    Signed-off-by: Chuck Lever <chuck.lever@oracle.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 3be6a462adcd5bd5a327164cd0ebb8543771798b
Author: Jeff Layton <jlayton@kernel.org>
Date:   Wed Jul 30 09:24:34 2025 -0400

    nfsd: track original timestamps in nfs4_delegation
    
    [ Upstream commit 7663e963a51122792811811c8119fd55c9ab254a ]
    
    As Trond points out [1], the "original time" mentioned in RFC 9754
    refers to the timestamps on the files at the time that the delegation
    was granted, and not the current timestamp of the file on the server.
    
    Store the current timestamps for the file in the nfs4_delegation when
    granting one. Add STATX_ATIME and STATX_MTIME to the request mask in
    nfs4_delegation_stat(). When granting OPEN_DELEGATE_READ_ATTRS_DELEG, do
    a nfs4_delegation_stat() and save the correct atime. If the stat() fails
    for any reason, fall back to granting a normal read deleg.
    
    [1]: https://lore.kernel.org/linux-nfs/47a4e40310e797f21b5137e847b06bb203d99e66.camel@kernel.org/
    
    Fixes: 7e13f4f8d27d ("nfsd: handle delegated timestamps in SETATTR")
    Signed-off-by: Jeff Layton <jlayton@kernel.org>
    Signed-off-by: Chuck Lever <chuck.lever@oracle.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit ab4e26c24f6e6e8b802d6c8df4be962b770f06ed
Author: Jeff Layton <jlayton@kernel.org>
Date:   Wed Jul 30 09:24:33 2025 -0400

    nfsd: use ATTR_CTIME_SET for delegated ctime updates
    
    [ Upstream commit c066ff58e5d6e5d7400e5fda0c33f95b8c37dd02 ]
    
    Ensure that notify_change() doesn't clobber a delegated ctime update
    with current_time() by setting ATTR_CTIME_SET for those updates.
    
    Don't bother setting the timestamps in cb_getattr_update_times() in the
    non-delegated case. notify_change() will do that itself.
    
    Fixes: 7e13f4f8d27d ("nfsd: handle delegated timestamps in SETATTR")
    Signed-off-by: Jeff Layton <jlayton@kernel.org>
    Signed-off-by: Chuck Lever <chuck.lever@oracle.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 0e2c499a459ebec2e6d4795eda857625983d722d
Author: Jeff Layton <jlayton@kernel.org>
Date:   Wed Jul 30 09:24:32 2025 -0400

    vfs: add ATTR_CTIME_SET flag
    
    [ Upstream commit afc5b36e29b95fbd31a60b9630d148857e5e513d ]
    
    When ATTR_ATIME_SET and ATTR_MTIME_SET are set in the ia_valid mask, the
    notify_change() logic takes that to mean that the request should set
    those values explicitly, and not override them with "now".
    
    With the advent of delegated timestamps, similar functionality is needed
    for the ctime. Add a ATTR_CTIME_SET flag, and use that to indicate that
    the ctime should be accepted as-is. Also, clean up the if statements to
    eliminate the extra negatives.
    
    In setattr_copy() and setattr_copy_mgtime() use inode_set_ctime_deleg()
    when ATTR_CTIME_SET is set, instead of basing the decision on ATTR_DELEG.
    
    Signed-off-by: Jeff Layton <jlayton@kernel.org>
    Signed-off-by: Chuck Lever <chuck.lever@oracle.com>
    Stable-dep-of: c066ff58e5d6 ("nfsd: use ATTR_CTIME_SET for delegated ctime updates")
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 910c7cdc8d5100b036c130c4351dab8b57a51c9f
Author: Jeff Layton <jlayton@kernel.org>
Date:   Wed Jul 30 09:24:31 2025 -0400

    nfsd: ignore ATTR_DELEG when checking ia_valid before notify_change()
    
    [ Upstream commit 5affb498e70bba3053b835c478a199bf92c99c4d ]
    
    If the only flag left is ATTR_DELEG, then there are no changes to be
    made.
    
    Fixes: 7e13f4f8d27d ("nfsd: handle delegated timestamps in SETATTR")
    Signed-off-by: Jeff Layton <jlayton@kernel.org>
    Signed-off-by: Chuck Lever <chuck.lever@oracle.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 18adf0702641c6a32523c97f5ccf94bd92ea7c62
Author: Jeff Layton <jlayton@kernel.org>
Date:   Wed Jul 30 09:24:30 2025 -0400

    nfsd: fix assignment of ia_ctime.tv_nsec on delegated mtime update
    
    [ Upstream commit 2990b5a47984c27873d165de9e88099deee95c8d ]
    
    The ia_ctime.tv_nsec field should be set to modify.nseconds.
    
    Fixes: 7e13f4f8d27d ("nfsd: handle delegated timestamps in SETATTR")
    Signed-off-by: Jeff Layton <jlayton@kernel.org>
    Signed-off-by: Chuck Lever <chuck.lever@oracle.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit af5dcd438728642a5fbe7c1d2d1c3e6afe6cb03f
Author: Fedor Pchelkin <pchelkin@ispras.ru>
Date:   Sat Apr 26 15:54:28 2025 +0300

    clk: tegra: do not overallocate memory for bpmp clocks
    
    [ Upstream commit 49ef6491106209c595476fc122c3922dfd03253f ]
    
    struct tegra_bpmp::clocks is a pointer to a dynamically allocated array
    of pointers to 'struct tegra_bpmp_clk'.
    
    But the size of the allocated area is calculated like it is an array
    containing actual 'struct tegra_bpmp_clk' objects - it's not true, there
    are just pointers.
    
    Found by Linux Verification Center (linuxtesting.org) with Svace static
    analysis tool.
    
    Fixes: 2db12b15c6f3 ("clk: tegra: Register clocks from root to leaf")
    Signed-off-by: Fedor Pchelkin <pchelkin@ispras.ru>
    Signed-off-by: Stephen Boyd <sboyd@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 530e1d53166ea51347e66d1fa6816899b351c2e5
Author: Alok Tiwari <alok.a.tiwari@oracle.com>
Date:   Sun Jul 6 13:11:55 2025 -0700

    clk: nxp: Fix pll0 rate check condition in LPC18xx CGU driver
    
    [ Upstream commit 1624dead9a4d288a594fdf19735ebfe4bb567cb8 ]
    
    The conditional check for the PLL0 multiplier 'm' used a logical AND
    instead of OR, making the range check ineffective. This patch replaces
    && with || to correctly reject invalid values of 'm' that are either
    less than or equal to 0 or greater than LPC18XX_PLL0_MSEL_MAX.
    
    This ensures proper bounds checking during clk rate setting and rounding.
    
    Fixes: b04e0b8fd544 ("clk: add lpc18xx cgu clk driver")
    Signed-off-by: Alok Tiwari <alok.a.tiwari@oracle.com>
    [sboyd@kernel.org: 'm' is unsigned so remove < condition]
    Signed-off-by: Stephen Boyd <sboyd@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit b7b40a7263bf73858dff0138260836fa02a22796
Author: Brian Masney <bmasney@redhat.com>
Date:   Mon Aug 11 11:18:29 2025 -0400

    clk: nxp: lpc18xx-cgu: convert from round_rate() to determine_rate()
    
    [ Upstream commit b46a3d323a5b7942e65025254c13801d0f475f02 ]
    
    The round_rate() clk ops is deprecated, so migrate this driver from
    round_rate() to determine_rate() using the Coccinelle semantic patch
    on the cover letter of this series.
    
    Signed-off-by: Brian Masney <bmasney@redhat.com>
    Stable-dep-of: 1624dead9a4d ("clk: nxp: Fix pll0 rate check condition in LPC18xx CGU driver")
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit a6270f88cc35b42cc04865dce5b0e509fa126d3d
Author: Chen-Yu Tsai <wenst@chromium.org>
Date:   Mon Aug 25 23:09:31 2025 +0800

    clk: mediatek: clk-mux: Do not pass flags to clk_mux_determine_rate_flags()
    
    [ Upstream commit 5e121370a7ad3414c7f3a77002e2b18abe5c6fe1 ]
    
    The `flags` in |struct mtk_mux| are core clk flags, not mux clk flags.
    Passing one to the other is wrong.
    
    Since there aren't any actual users adding CLK_MUX_* flags, just drop it
    for now.
    
    Fixes: b05ea3314390 ("clk: mediatek: clk-mux: Add .determine_rate() callback")
    Signed-off-by: Chen-Yu Tsai <wenst@chromium.org>
    Signed-off-by: Stephen Boyd <sboyd@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit fe3e0b0167e0fea5557167ffae2d161d50fd8705
Author: AngeloGioacchino Del Regno <angelogioacchino.delregno@collabora.com>
Date:   Thu Jul 24 10:38:28 2025 +0200

    clk: mediatek: mt8195-infra_ao: Fix parent for infra_ao_hdmi_26m
    
    [ Upstream commit 6c4c26b624790098988c1034541087e3e5ed5bed ]
    
    The infrastructure gate for the HDMI specific crystal needs the
    top_hdmi_xtal clock to be configured in order to ungate the 26m
    clock to the HDMI IP, and it wouldn't work without.
    
    Reparent the infra_ao_hdmi_26m clock to top_hdmi_xtal to fix that.
    
    Fixes: e2edf59dec0b ("clk: mediatek: Add MT8195 infrastructure clock support")
    Signed-off-by: AngeloGioacchino Del Regno <angelogioacchino.delregno@collabora.com>
    Signed-off-by: Stephen Boyd <sboyd@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 5b965ec2ef65ba5bf806cbfdfa6277065517dd7e
Author: Ian Rogers <irogers@google.com>
Date:   Thu Sep 18 10:24:16 2025 -0700

    perf build-id: Ensure snprintf string is empty when size is 0
    
    [ Upstream commit 0dc96cae063cbf9ebf6631b33b08e9ba02324248 ]
    
    The string result of build_id__snprintf() is unconditionally used in
    places like dsos__fprintf_buildid_cb(). If the build id has size 0 then
    this creates a use of uninitialized memory. Add null termination for the
    size 0 case.
    
    A similar fix was written by Jiri Olsa in commit 6311951d4f8f28c4 ("perf
    tools: Initialize output buffer in build_id__sprintf") but lost in the
    transition to snprintf.
    
    Fixes: fccaaf6fbbc59910 ("perf build-id: Change sprintf functions to snprintf")
    Signed-off-by: Ian Rogers <irogers@google.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Howard Chu <howardchu95@gmail.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: James Clark <james.clark@linaro.org>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 8887629b27b1c1aa727ea96e231bdbad46416cc1
Author: Ian Rogers <irogers@google.com>
Date:   Thu Sep 18 10:24:15 2025 -0700

    perf evsel: Ensure the fallback message is always written to
    
    [ Upstream commit 24937ee839e4bbc097acde73eeed67812bad2d99 ]
    
    The fallback message is unconditionally printed in places like
    record__open().
    
    If no fallback is attempted this can lead to printing uninitialized
    data, crashes, etc.
    
    Fixes: c0a54341c0e89333 ("perf evsel: Introduce event fallback method")
    Signed-off-by: Ian Rogers <irogers@google.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Howard Chu <howardchu95@gmail.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: James Clark <james.clark@linaro.org>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 13d62dcae94060cd2fb0f587f1c5e9c8585b375b
Author: Ian Rogers <irogers@google.com>
Date:   Thu Sep 18 15:22:02 2025 -0700

    perf test: Avoid uncore_imc/clockticks in uniquification test
    
    [ Upstream commit edaeb4bcf1511fe4e464fff9dd4a3abf6b0096da ]
    
    The detection of uncore_imc may happen for free running PMUs and the
    clockticks event may be present on uncore_clock. Rewrite the test to
    detect duplicated/deduplicated events from perf list, not hardcoded to
    uncore_imc.
    
    If perf stat fails then assume it is permissions and skip the test.
    
    Committer testing:
    
    Before:
    
      root@x1:~# perf test -vv uniquifyi
       96: perf stat events uniquifying:
      --- start ---
      test child forked, pid 220851
      stat event uniquifying test
      grep: Unmatched [, [^, [:, [., or [=
      Event is not uniquified [Failed]
      perf stat -e clockticks -A -o /tmp/__perf_test.stat_output.X7ChD -- true
      # started on Fri Sep 19 16:48:38 2025
    
       Performance counter stats for 'system wide':
    
      CPU0            2,310,956      uncore_clock/clockticks/
    
             0.001746771 seconds time elapsed
    
      ---- end(-1) ----
       96: perf stat events uniquifying                                    : FAILED!
      root@x1:~#
    
    After:
    
      root@x1:~# perf test -vv uniquifyi
       96: perf stat events uniquifying:
      --- start ---
      test child forked, pid 222366
      Uniquification of PMU sysfs events test
      Testing event uncore_imc_free_running/data_read/ is uniquified to uncore_imc_free_running_0/data_read/
      Testing event uncore_imc_free_running/data_total/ is uniquified to uncore_imc_free_running_0/data_total/
      Testing event uncore_imc_free_running/data_write/ is uniquified to uncore_imc_free_running_0/data_write/
      Testing event uncore_imc_free_running/data_read/ is uniquified to uncore_imc_free_running_1/data_read/
      Testing event uncore_imc_free_running/data_total/ is uniquified to uncore_imc_free_running_1/data_total/
      Testing event uncore_imc_free_running/data_write/ is uniquified to uncore_imc_free_running_1/data_write/
      ---- end(0) ----
       96: perf stat events uniquifying                                    : Ok
      root@x1:~#
    
    Fixes: 070b315333ee942f ("perf test: Restrict uniquifying test to machines with 'uncore_imc'")
    Signed-off-by: Ian Rogers <irogers@google.com>
    Tested-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Athira Rajeev <atrajeev@linux.ibm.com>
    Cc: Chun-Tse Shao <ctshao@google.com>
    Cc: Howard Chu <howardchu95@gmail.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: James Clark <james.clark@linaro.org>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit c021b53c6b584aea08270a6db6785ecddc4eda55
Author: Ian Rogers <irogers@google.com>
Date:   Thu Sep 18 15:22:01 2025 -0700

    perf evsel: Fix uniquification when PMU given without suffix
    
    [ Upstream commit 693101792e45eefc888c7ba10b91108047399f5d ]
    
    The PMU name is appearing twice in:
    ```
    $ perf stat -e uncore_imc_free_running/data_total/ -A true
    
     Performance counter stats for 'system wide':
    
    CPU0                 1.57 MiB  uncore_imc_free_running_0/uncore_imc_free_running,data_total/
    CPU0                 1.58 MiB  uncore_imc_free_running_1/uncore_imc_free_running,data_total/
           0.000892376 seconds time elapsed
    ```
    
    Use the pmu_name_len_no_suffix to avoid this problem.
    
    Committer testing:
    
    After this patch:
    
      root@x1:~# perf stat -e uncore_imc_free_running/data_total/ -A true
    
       Performance counter stats for 'system wide':
    
      CPU0                 1.69 MiB  uncore_imc_free_running_0/data_total/
      CPU0                 1.68 MiB  uncore_imc_free_running_1/data_total/
    
             0.002141605 seconds time elapsed
    
      root@x1:~#
    
    Fixes: 7d45f402d3117e0b ("perf evlist: Make uniquifying counter names consistent")
    Signed-off-by: Ian Rogers <irogers@google.com>
    Tested-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Athira Rajeev <atrajeev@linux.ibm.com>
    Cc: Chun-Tse Shao <ctshao@google.com>
    Cc: Howard Chu <howardchu95@gmail.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: James Clark <james.clark@linaro.org>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 28281ffe64fd41019753a9b6267e72209b8773da
Author: Ian Rogers <irogers@google.com>
Date:   Thu Sep 18 15:22:00 2025 -0700

    perf test: Don't leak workload gopipe in PERF_RECORD_*
    
    [ Upstream commit 48918cacefd226af44373e914e63304927c0e7dc ]
    
    The test starts a workload and then opens events. If the events fail
    to open, for example because of perf_event_paranoid, the gopipe of the
    workload is leaked and the file descriptor leak check fails when the
    test exits. To avoid this cancel the workload when opening the events
    fails.
    
    Before:
    ```
    $ perf test -vv 7
      7: PERF_RECORD_* events & perf_sample fields:
     --- start ---
    test child forked, pid 1189568
    Using CPUID GenuineIntel-6-B7-1
     ------------------------------------------------------------
    perf_event_attr:
      type                             0 (PERF_TYPE_HARDWARE)
      config                           0xa00000000 (cpu_atom/PERF_COUNT_HW_CPU_CYCLES/)
      disabled                         1
     ------------------------------------------------------------
    sys_perf_event_open: pid 0  cpu -1  group_fd -1  flags 0x8
    sys_perf_event_open failed, error -13
     ------------------------------------------------------------
    perf_event_attr:
      type                             0 (PERF_TYPE_HARDWARE)
      config                           0xa00000000 (cpu_atom/PERF_COUNT_HW_CPU_CYCLES/)
      disabled                         1
      exclude_kernel                   1
     ------------------------------------------------------------
    sys_perf_event_open: pid 0  cpu -1  group_fd -1  flags 0x8 = 3
     ------------------------------------------------------------
    perf_event_attr:
      type                             0 (PERF_TYPE_HARDWARE)
      config                           0x400000000 (cpu_core/PERF_COUNT_HW_CPU_CYCLES/)
      disabled                         1
     ------------------------------------------------------------
    sys_perf_event_open: pid 0  cpu -1  group_fd -1  flags 0x8
    sys_perf_event_open failed, error -13
     ------------------------------------------------------------
    perf_event_attr:
      type                             0 (PERF_TYPE_HARDWARE)
      config                           0x400000000 (cpu_core/PERF_COUNT_HW_CPU_CYCLES/)
      disabled                         1
      exclude_kernel                   1
     ------------------------------------------------------------
    sys_perf_event_open: pid 0  cpu -1  group_fd -1  flags 0x8 = 3
    Attempt to add: software/cpu-clock/
    ..after resolving event: software/config=0/
    cpu-clock -> software/cpu-clock/
     ------------------------------------------------------------
    perf_event_attr:
      type                             1 (PERF_TYPE_SOFTWARE)
      size                             136
      config                           0x9 (PERF_COUNT_SW_DUMMY)
      sample_type                      IP|TID|TIME|CPU
      read_format                      ID|LOST
      disabled                         1
      inherit                          1
      mmap                             1
      comm                             1
      enable_on_exec                   1
      task                             1
      sample_id_all                    1
      mmap2                            1
      comm_exec                        1
      ksymbol                          1
      bpf_event                        1
      { wakeup_events, wakeup_watermark } 1
     ------------------------------------------------------------
    sys_perf_event_open: pid 1189569  cpu 0  group_fd -1  flags 0x8
    sys_perf_event_open failed, error -13
    perf_evlist__open: Permission denied
     ---- end(-2) ----
    Leak of file descriptor 6 that opened: 'pipe:[14200347]'
     ---- unexpected signal (6) ----
    iFailed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
    Failed to read build ID for //anon
        #0 0x565358f6666e in child_test_sig_handler builtin-test.c:311
        #1 0x7f29ce849df0 in __restore_rt libc_sigaction.c:0
        #2 0x7f29ce89e95c in __pthread_kill_implementation pthread_kill.c:44
        #3 0x7f29ce849cc2 in raise raise.c:27
        #4 0x7f29ce8324ac in abort abort.c:81
        #5 0x565358f662d4 in check_leaks builtin-test.c:226
        #6 0x565358f6682e in run_test_child builtin-test.c:344
        #7 0x565358ef7121 in start_command run-command.c:128
        #8 0x565358f67273 in start_test builtin-test.c:545
        #9 0x565358f6771d in __cmd_test builtin-test.c:647
        #10 0x565358f682bd in cmd_test builtin-test.c:849
        #11 0x565358ee5ded in run_builtin perf.c:349
        #12 0x565358ee6085 in handle_internal_command perf.c:401
        #13 0x565358ee61de in run_argv perf.c:448
        #14 0x565358ee6527 in main perf.c:555
        #15 0x7f29ce833ca8 in __libc_start_call_main libc_start_call_main.h:74
        #16 0x7f29ce833d65 in __libc_start_main@@GLIBC_2.34 libc-start.c:128
        #17 0x565358e391c1 in _start perf[851c1]
      7: PERF_RECORD_* events & perf_sample fields                       : FAILED!
    ```
    
    After:
    ```
    $ perf test 7
      7: PERF_RECORD_* events & perf_sample fields                       : Skip (permissions)
    ```
    
    Fixes: 16d00fee703866c6 ("perf tests: Move test__PERF_RECORD into separate object")
    Signed-off-by: Ian Rogers <irogers@google.com>
    Tested-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Athira Rajeev <atrajeev@linux.ibm.com>
    Cc: Chun-Tse Shao <ctshao@google.com>
    Cc: Howard Chu <howardchu95@gmail.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: James Clark <james.clark@linaro.org>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit f57d0356825625cb822827ab14feb98bfc6843f6
Author: Leo Yan <leo.yan@arm.com>
Date:   Fri Aug 8 14:24:40 2025 +0100

    perf session: Fix handling when buffer exceeds 2 GiB
    
    [ Upstream commit c17dda8013495d8132c976cbf349be9949d0fbd1 ]
    
    If a user specifies an AUX buffer larger than 2 GiB, the returned size
    may exceed 0x80000000. Since the err variable is defined as a signed
    32-bit integer, such a value overflows and becomes negative.
    
    As a result, the perf record command reports an error:
    
      0x146e8 [0x30]: failed to process type: 71 [Unknown error 183711232]
    
    Change the type of the err variable to a signed 64-bit integer to
    accommodate large buffer sizes correctly.
    
    Fixes: d5652d865ea734a1 ("perf session: Add ability to skip 4GiB or more")
    Reported-by: Tamas Zsoldos <tamas.zsoldos@arm.com>
    Signed-off-by: Leo Yan <leo.yan@arm.com>
    Acked-by: Namhyung Kim <namhyung@kernel.org>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Ian Rogers <irogers@google.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Link: https://lore.kernel.org/r/20250808-perf_fix_big_buffer_size-v1-1-45f45444a9a4@arm.com
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 1f823c6709803f1a86f129fa066b674ea2f7cab5
Author: Fushuai Wang <wangfushuai@baidu.com>
Date:   Wed Sep 17 17:54:22 2025 +0800

    perf trace: Fix IS_ERR() vs NULL check bug
    
    [ Upstream commit b0f4ade163e551d0c470ead7ac57eaf373eec71a ]
    
    The alloc_syscall_stats() function always returns an error pointer
    (ERR_PTR) on failure.
    
    So replace NULL check with IS_ERR() check after calling
    alloc_syscall_stats() function.
    
    Fixes: fc00897c8a3f7f57 ("perf trace: Add --summary-mode option")
    Reviewed-by: Ian Rogers <irogers@google.com>
    Signed-off-by: Fushuai Wang <wangfushuai@baidu.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 855a8ef10f0a60938de720ee7135ac3a9c31e116
Author: Ian Rogers <irogers@google.com>
Date:   Thu Aug 21 15:18:31 2025 -0700

    perf test shell lbr: Avoid failures with perf event paranoia
    
    [ Upstream commit 48314d20fe467d6653783cbf5536cb2fcc9bdd7c ]
    
    When not running as root and with higher perf event paranoia values
    the perf record LBR tests could fail rather than skipping the
    problematic tests.
    
    Add the sensitivity to the test and confirm it passes with paranoia
    values from -1 to 2.
    
    Committer testing:
    
    Testing with '$ perf test -vv lbr', i.e. as non root, and then comparing
    the output shows the mentioned errors before this patch:
    
      acme@x1:~$ grep -m1 "model name" /proc/cpuinfo
      model name    : 13th Gen Intel(R) Core(TM) i7-1365U
      acme@x1:~$
    
    Before:
    
     132: perf record LBR tests            : Skip
    
    After:
    
     132: perf record LBR tests            : Ok
    
    Fixes: 32559b99e0f59070 ("perf test: Add set of perf record LBR tests")
    Signed-off-by: Ian Rogers <irogers@google.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Chun-Tse Shao <ctshao@google.com>
    Cc: Howard Chu <howardchu95@gmail.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: James Clark <james.clark@linaro.org>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit ee3a9fc11cd03f2c4beee35c48658303c26e58e4
Author: Ian Rogers <irogers@google.com>
Date:   Fri Sep 12 17:03:50 2025 -0700

    perf test: AMD IBS swfilt skip kernel tests if paranoia is >1
    
    [ Upstream commit 2e3501212293c5005873c6ca6bb4f963a7eec442 ]
    
    If not root and the perf_event_paranoid is set >1 swfilt will fail to
    open the event failing the test. Add check to skip the test in that
    case.
    
    Fixes: 0e71bcdcf1f0b10b ("perf test: Add AMD IBS sw filter test")
    Reviewed-by: Namhyung Kim <namhyung@kernel.org>
    Signed-off-by: Ian Rogers <irogers@google.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Collin Funk <collin.funk1@gmail.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: James Clark <james.clark@linaro.org>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Cc: Ravi Bangoria <ravi.bangoria@amd.com>
    Link: https://lore.kernel.org/r/20250913000350.1306948-1-irogers@google.com
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit a0d8871492d536ddc623cf1e4be0aad9784216f0
Author: Ilkka Koskinen <ilkka@os.amperecomputing.com>
Date:   Wed Sep 10 12:52:12 2025 -0700

    perf vendor events arm64 AmpereOneX: Fix typo - should be l1d_cache_access_prefetches
    
    [ Upstream commit 97996580da08f06f8b09a86f3384ed9fa7a52e32 ]
    
    Add missing 'h' to l1d_cache_access_prefetces
    
    Also fix a couple of typos and use consistent term in brief descriptions
    
    Fixes: 16438b652b464ef7 ("perf vendor events arm64 AmpereOneX: Add core PMU events and metrics")
    Reviewed-by: James Clark <james.clark@linaro.org>
    Signed-off-by: Ilkka Koskinen <ilkka@os.amperecomputing.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Ian Rogers <irogers@google.com>
    Cc: Ilkka Koskinen <ilkka@os.amperecomputing.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: John Garry <john.g.garry@oracle.com>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Leo Yan <leo.yan@linux.dev>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Mike Leach <mike.leach@linaro.org>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Cc: Will Deacon <will@kernel.org>
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit eea105d685b3b3c0e7de2364b6e48697e12bd0df
Author: Leo Yan <leo.yan@arm.com>
Date:   Fri Sep 12 16:42:09 2025 +0100

    perf arm_spe: Correct memory level for remote access
    
    [ Upstream commit cb300e3515057fb555983ce47e8acc86a5c69c3c ]
    
    For remote accesses, the data source packet does not contain information
    about the memory level. To avoid misinformation, set the memory level to
    NA (Not Available).
    
    Fixes: 4e6430cbb1a9f1dc ("perf arm-spe: Use SPE data source for neoverse cores")
    Reviewed-by: James Clark <james.clark@linaro.org>
    Signed-off-by: Leo Yan <leo.yan@arm.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Ali Saidi <alisaidi@amazon.com>
    Cc: German Gomez <german.gomez@arm.com>
    Cc: Ian Rogers <irogers@google.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Will Deacon <will@kernel.org>
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit c7be909be16cf07208fd97faa498e14416407f96
Author: Leo Yan <leo.yan@arm.com>
Date:   Fri Sep 12 16:42:08 2025 +0100

    perf arm_spe: Correct setting remote access
    
    [ Upstream commit 039fd0634a0629132432632d7ac9a14915406b5c ]
    
    Set the mem_remote field for a remote access to appropriately represent
    the event.
    
    Fixes: a89dbc9b988f3ba8 ("perf arm-spe: Set sample's data source field")
    Reviewed-by: James Clark <james.clark@linaro.org>
    Signed-off-by: Leo Yan <leo.yan@arm.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Ali Saidi <alisaidi@amazon.com>
    Cc: German Gomez <german.gomez@arm.com>
    Cc: Ian Rogers <irogers@google.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Will Deacon <will@kernel.org>
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit f9d4ec7d13777393303d4846dc58a4b8457f1130
Author: Clément Le Goffic <clement.legoffic@foss.st.com>
Date:   Tue Jul 15 16:07:13 2025 +0200

    rtc: optee: fix memory leak on driver removal
    
    [ Upstream commit a531350d2fe58f7fc4516e555f22391dee94efd9 ]
    
    Fix a memory leak in case of driver removal.
    Free the shared memory used for arguments exchanges between kernel and
    OP-TEE RTC PTA.
    
    Fixes: 81c2f059ab90 ("rtc: optee: add RTC driver for OP-TEE RTC PTA")
    Signed-off-by: Clément Le Goffic <clement.legoffic@foss.st.com>
    Link: https://lore.kernel.org/r/20250715-upstream-optee-rtc-v1-1-e0fdf8aae545@foss.st.com
    Signed-off-by: Alexandre Belloni <alexandre.belloni@bootlin.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 646e5f4c88a28bf73eae396e254f7456fee10a03
Author: Rob Herring (Arm) <robh@kernel.org>
Date:   Thu Aug 21 16:57:02 2025 -0500

    rtc: x1205: Fix Xicor X1205 vendor prefix
    
    [ Upstream commit 606d19ee37de3a72f1b6e95a4ea544f6f20dbb46 ]
    
    The vendor for the X1205 RTC is not Xircom, but Xicor which was acquired
    by Intersil. Since the I2C subsystem drops the vendor prefix for driver
    matching, the vendor prefix hasn't mattered.
    
    Fixes: 6875404fdb44 ("rtc: x1205: Add DT probing support")
    Signed-off-by: Rob Herring (Arm) <robh@kernel.org>
    Reviewed-by: Linus Walleij <linus.walleij@linaro.org>
    Link: https://lore.kernel.org/r/20250821215703.869628-2-robh@kernel.org
    Signed-off-by: Alexandre Belloni <alexandre.belloni@bootlin.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 642356ee6e3c661a660d37ac81b72864b556d753
Author: Yunseong Kim <ysk@kzalloc.com>
Date:   Fri Aug 22 16:25:08 2025 +0000

    perf util: Fix compression checks returning -1 as bool
    
    [ Upstream commit 43fa1141e2c1af79c91aaa4df03e436c415a6fc3 ]
    
    The lzma_is_compressed and gzip_is_compressed functions are declared
    to return a "bool" type, but in case of an error (e.g., file open
    failure), they incorrectly returned -1.
    
    A bool type is a boolean value that is either true or false.
    Returning -1 for a bool return type can lead to unexpected behavior
    and may violate strict type-checking in some compilers.
    
    Fix the return value to be false in error cases, ensuring the function
    adheres to its declared return type improves for preventing potential
    bugs related to type mismatch.
    
    Fixes: 4b57fd44b61beb51 ("perf tools: Add lzma_is_compressed function")
    Reviewed-by: Ian Rogers <irogers@google.com>
    Signed-off-by: Yunseong Kim <ysk@kzalloc.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Stephen Brennan <stephen.s.brennan@oracle.com>
    Link: https://lore.kernel.org/r/20250822162506.316844-3-ysk@kzalloc.com
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 3bec6565ecc257093a7ada4b6cff42f5956ecd0c
Author: GuoHan Zhao <zhaoguohan@kylinos.cn>
Date:   Mon Sep 8 14:52:03 2025 +0800

    perf drm_pmu: Fix fd_dir leaks in for_each_drm_fdinfo_in_dir()
    
    [ Upstream commit baa03483fdf3545f2b223a4ca775e1938d956284 ]
    
    Fix file descriptor leak when callback function returns error. The
    function was directly returning without closing fdinfo_dir_fd and
    fd_dir when cb() returned non-zero value.
    
    Fixes: 28917cb17f9df9c2 ("perf drm_pmu: Add a tool like PMU to expose DRM information")
    Reviewed-by: Ian Rogers <irogers@google.com>
    Reviewed-by: Markus Elfring <Markus.Elfring@web.de>
    Reviewed-by: Namhyung Kim <namhyung@kernel.org>
    Signed-off-by: GuoHan Zhao <zhaoguohan@kylinos.cn>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Link: https://lore.kernel.org/r/20250908065203.22187-1-zhaoguohan@kylinos.cn
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 0ca35ac560305ccfa76e4cca97e456c6acaf32a4
Author: Christophe Leroy <christophe.leroy@csgroup.eu>
Date:   Mon Aug 18 11:57:15 2025 +0200

    perf: Completely remove possibility to override MAX_NR_CPUS
    
    [ Upstream commit 6f8fb022ef2c6694e47f6e2f5676eb63be66c208 ]
    
    Commit 21b8732eb447 ("perf tools: Allow overriding MAX_NR_CPUS at
    compile time") added the capability to override MAX_NR_CPUS. At
    that time it was necessary to reduce the huge amount of RAM used
    by static stats variables.
    
    But this has been unnecessary since commit 6a1e2c5c2673 ("perf stat:
    Remove a set of shadow stats static variables"), and
    commit e8399d34d568 ("libperf cpumap: Hide/reduce scope of
    MAX_NR_CPUS") broke the build in that case because it failed to
    add the guard around the new definition of MAX_NR_CPUS.
    
    So cleanup things and remove guards completely to officialise it
    is not necessary anymore to override MAX_NR_CPUS.
    
    Fixes: e8399d34d568d61c ("libperf cpumap: Hide/reduce scope of MAX_NR_CPUS")
    Signed-off-by: Christophe Leroy <christophe.leroy@csgroup.eu>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Ian Rogers <irogers@google.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Leo Yan <leo.yan@arm.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Link: https://lore.kernel.org/all/8c8553387ebf904a9e5a93eaf643cb01164d9fb3.1736188471.git.christophe.leroy@csgroup.eu/
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit fd30ee99398e66a597c5a0fb9cc623ab634dd17b
Author: Yuan CHen <chenyuan@kylinos.cn>
Date:   Mon Sep 8 02:28:10 2025 +0100

    clk: renesas: cpg-mssr: Fix memory leak in cpg_mssr_reserved_init()
    
    [ Upstream commit cc55fc58fc1b7f405003fd2ecf79e74653461f0b ]
    
    In case of krealloc_array() failure, the current error handling just
    returns from the function without freeing the original array.
    Fix this memory leak by freeing the original array.
    
    Fixes: 6aa1754764901668 ("clk: renesas: cpg-mssr: Ignore all clocks assigned to non-Linux system")
    Signed-off-by: Yuan CHen <chenyuan@kylinos.cn>
    Reviewed-by: Geert Uytterhoeven <geert+renesas@glider.be>
    Link: https://patch.msgid.link/20250908012810.4767-1-chenyuan_fl@163.com
    Signed-off-by: Geert Uytterhoeven <geert+renesas@glider.be>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 62fc9ae12ed0110d96abf784e7a375f0703d8182
Author: Brian Masney <bmasney@redhat.com>
Date:   Mon Aug 11 11:17:53 2025 -0400

    clk: at91: peripheral: fix return value
    
    [ Upstream commit 47b13635dabc14f1c2fdcaa5468b47ddadbdd1b5 ]
    
    determine_rate() is expected to return an error code, or 0 on success.
    clk_sam9x5_peripheral_determine_rate() has a branch that returns the
    parent rate on a certain case. This is the behavior of round_rate(),
    so let's go ahead and fix this by setting req->rate.
    
    Fixes: b4c115c76184f ("clk: at91: clk-peripheral: add support for changeable parent rate")
    Reviewed-by: Alexander Sverdlin <alexander.sverdlin@gmail.com>
    Acked-by: Nicolas Ferre <nicolas.ferre@microchip.com>
    Signed-off-by: Brian Masney <bmasney@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit fc2da4a15c3ef873ed8c3dd780cf9817f9f3f29e
Author: Ian Rogers <irogers@google.com>
Date:   Mon Aug 18 12:03:57 2025 -0700

    perf parse-events: Handle fake PMUs in CPU terms
    
    [ Upstream commit 1a461a62fb422db9cf870a4f184885cc69873b7f ]
    
    The "Parsing of PMU event table metrics with fake PMUs" will test
    metrics on machines/models that may be missing a PMU, in such a case
    the fake_pmu should be used to avoid errors.
    
    Metrics that get the cpumask from a different PMU, such as
    "tsc/cpu=cpu_atom/", also need to be resilient in this test.
    
    The parse_events_state fake_pmu is set when missing PMUs should be
    ignored.
    
    So that it can be queried, pass it to the config term functions, as well
    as to get_config_cpu, then ignore failures when fake_pmu is set.
    
    Some minor code refactoring to cut down on the indent and remove some
    redundant checks.
    
    Fixes: bd741d80dc65922c ("perf parse-events: Allow the cpu term to be a PMU or CPU range")
    Signed-off-by: Ian Rogers <irogers@google.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Andreas Färber <afaerber@suse.de>
    Cc: Caleb Biggers <caleb.biggers@intel.com>
    Cc: Ian Rogers <irogers@google.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: linux-actions@lists.infradead.org
    Cc: Manivannan Sadhasivam <mani@kernel.org>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Cc: Thomas Falcon <thomas.falcon@intel.com>
    Cc: Weilin Wang <weilin.wang@intel.com>
    Link: https://lore.kernel.org/r/20250818190416.145274-2-irogers@google.com
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 2da625d47badb36223a9ea71d48838976a69fa8c
Author: Lukas Bulwahn <lukas.bulwahn@redhat.com>
Date:   Tue Sep 2 14:17:54 2025 +0200

    clk: qcom: Select the intended config in QCS_DISPCC_615
    
    [ Upstream commit 9524f95c4042545ee8fc3191b9b89c61a1aca6fb ]
    
    Commit 9b47105f5434 ("clk: qcom: dispcc-qcs615: Add QCS615 display clock
    controller driver") adds the config QCS_DISPCC_615, which selects the
    non-existing config QCM_GCC_615. Probably, this is just a three-letter
    abbreviation mix-up here, though. There is a config named QCS_GCC_615,
    and the related config QCS_CAMCC_615 selects that config.
    
    Fix the typo and use the intended config name in the select command.
    
    Fixes: 9b47105f5434 ("clk: qcom: dispcc-qcs615: Add QCS615 display clock controller driver")
    Signed-off-by: Lukas Bulwahn <lukas.bulwahn@redhat.com>
    Reviewed-by: Imran Shaik <imran.shaik@oss.qualcomm.com>
    Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@oss.qualcomm.com>
    Link: https://lore.kernel.org/r/20250902121754.277452-1-lukas.bulwahn@redhat.com
    Signed-off-by: Bjorn Andersson <andersson@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 84203d2bf5d11ada87a3084eb988406d968041d5
Author: Dan Carpenter <dan.carpenter@linaro.org>
Date:   Tue Sep 2 09:33:36 2025 +0300

    clk: qcom: common: Fix NULL vs IS_ERR() check in qcom_cc_icc_register()
    
    [ Upstream commit 1e50f5c9965252ed6657b8692cd7366784d60616 ]
    
    The devm_clk_hw_get_clk() function doesn't return NULL, it returns error
    pointers.  Update the checking to match.
    
    Fixes: 8737ec830ee3 ("clk: qcom: common: Add interconnect clocks support")
    Signed-off-by: Dan Carpenter <dan.carpenter@linaro.org>
    Reviewed-by: Imran Shaik <imran.shaik@oss.qualcomm.com>
    Reviewed-by: Konrad Dybcio <konrad.dybcio@oss.qualcomm.com>
    Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@linaro.org>
    Link: https://lore.kernel.org/r/aLaPwL2gFS85WsfD@stanley.mountain
    Signed-off-by: Bjorn Andersson <andersson@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit fbd0890e88479e379133fe4287039cac1d83b4a6
Author: Ian Rogers <irogers@google.com>
Date:   Thu Aug 21 09:38:19 2025 -0700

    libperf event: Ensure tracing data is multiple of 8 sized
    
    [ Upstream commit b39c915a4f365cce6bdc0e538ed95d31823aea8f ]
    
    Perf's synthetic-events.c will ensure 8-byte alignment of tracing
    data, writing it after a perf_record_header_tracing_data event.
    
    Add padding to struct perf_record_header_tracing_data to make it 16-byte
    rather than 12-byte sized.
    
    Fixes: 055c67ed39887c55 ("perf tools: Move event synthesizing routines to separate .c file")
    Reviewed-by: James Clark <james.clark@linaro.org>
    Signed-off-by: Ian Rogers <irogers@google.com>
    Acked-by: Namhyung Kim <namhyung@kernel.org>
    Tested-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Athira Rajeev <atrajeev@linux.ibm.com>
    Cc: Blake Jones <blakejones@google.com>
    Cc: Chun-Tse Shao <ctshao@google.com>
    Cc: Collin Funk <collin.funk1@gmail.com>
    Cc: Howard Chu <howardchu95@gmail.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: Jan Polensky <japo@linux.ibm.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Li Huafei <lihuafei1@huawei.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Nam Cao <namcao@linutronix.de>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Cc: Steinar H. Gunderson <sesse@google.com>
    Cc: Thomas Gleixner <tglx@linutronix.de>
    Link: https://lore.kernel.org/r/20250821163820.1132977-6-irogers@google.com
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 032aa8bb5bc5bff31d5ea2ded5a4f97099e46e88
Author: Ian Rogers <irogers@google.com>
Date:   Thu Aug 21 09:38:17 2025 -0700

    perf evsel: Avoid container_of on a NULL leader
    
    [ Upstream commit 2354479026d726954ff86ce82f4b649637319661 ]
    
    An evsel should typically have a leader of itself, however, in tests
    like 'Sample parsing' a NULL leader may occur and the container_of
    will return a corrupt pointer.
    
    Avoid this with an explicit NULL test.
    
    Fixes: fba7c86601e2e42d ("libperf: Move 'leader' from tools/perf to perf_evsel::leader")
    Reviewed-by: James Clark <james.clark@linaro.org>
    Signed-off-by: Ian Rogers <irogers@google.com>
    Acked-by: Namhyung Kim <namhyung@kernel.org>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Athira Rajeev <atrajeev@linux.ibm.com>
    Cc: Blake Jones <blakejones@google.com>
    Cc: Chun-Tse Shao <ctshao@google.com>
    Cc: Collin Funk <collin.funk1@gmail.com>
    Cc: Howard Chu <howardchu95@gmail.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: Jan Polensky <japo@linux.ibm.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Li Huafei <lihuafei1@huawei.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Nam Cao <namcao@linutronix.de>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Cc: Steinar H. Gunderson <sesse@google.com>
    Cc: Thomas Gleixner <tglx@linutronix.de>
    Link: https://lore.kernel.org/r/20250821163820.1132977-4-irogers@google.com
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 5206dd28066e15dbf64b620bc8f92034a9f3a747
Author: Ian Rogers <irogers@google.com>
Date:   Thu Aug 21 09:38:16 2025 -0700

    perf test trace_btf_enum: Skip if permissions are insufficient
    
    [ Upstream commit 4bd5bd8dbd41a208fb73afb65bda6f38e2b5a637 ]
    
    Modify test behavior to skip if BPF calls fail with "Operation not
    permitted".
    
    Fixes: d66763fed30f0bd8 ("perf test trace_btf_enum: Add regression test for the BTF augmentation of enums in 'perf trace'")
    Reviewed-by: James Clark <james.clark@linaro.org>
    Signed-off-by: Ian Rogers <irogers@google.com>
    Acked-by: Namhyung Kim <namhyung@kernel.org>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Athira Rajeev <atrajeev@linux.ibm.com>
    Cc: Blake Jones <blakejones@google.com>
    Cc: Chun-Tse Shao <ctshao@google.com>
    Cc: Collin Funk <collin.funk1@gmail.com>
    Cc: Howard Chu <howardchu95@gmail.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: Jan Polensky <japo@linux.ibm.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Li Huafei <lihuafei1@huawei.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Nam Cao <namcao@linutronix.de>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Cc: Steinar H. Gunderson <sesse@google.com>
    Cc: Thomas Gleixner <tglx@linutronix.de>
    Link: https://lore.kernel.org/r/20250821163820.1132977-3-irogers@google.com
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit b9bfbcead73f16575384df93bdde1dd3fe7ab91e
Author: Ian Rogers <irogers@google.com>
Date:   Thu Aug 21 09:38:15 2025 -0700

    perf disasm: Avoid undefined behavior in incrementing NULL
    
    [ Upstream commit 78d853512d6f979cf0cc41566e4f6cd82995ff34 ]
    
    Incrementing NULL is undefined behavior and triggers ubsan during the
    perf annotate test.
    
    Split a compound statement over two lines to avoid this.
    
    Fixes: 98f69a573c668a18 ("perf annotate: Split out util/disasm.c")
    Reviewed-by: Collin Funk <collin.funk1@gmail.com>
    Reviewed-by: James Clark <james.clark@linaro.org>
    Reviewed-by: Kuan-Wei Chiu <visitorckw@gmail.com>
    Signed-off-by: Ian Rogers <irogers@google.com>
    Acked-by: Namhyung Kim <namhyung@kernel.org>
    Cc: Adrian Hunter <adrian.hunter@intel.com>
    Cc: Alexander Shishkin <alexander.shishkin@linux.intel.com>
    Cc: Athira Rajeev <atrajeev@linux.ibm.com>
    Cc: Blake Jones <blakejones@google.com>
    Cc: Chun-Tse Shao <ctshao@google.com>
    Cc: Howard Chu <howardchu95@gmail.com>
    Cc: Ingo Molnar <mingo@redhat.com>
    Cc: Jan Polensky <japo@linux.ibm.com>
    Cc: Jiri Olsa <jolsa@kernel.org>
    Cc: Kan Liang <kan.liang@linux.intel.com>
    Cc: Li Huafei <lihuafei1@huawei.com>
    Cc: Mark Rutland <mark.rutland@arm.com>
    Cc: Nam Cao <namcao@linutronix.de>
    Cc: Namhyung Kim <namhyung@kernel.org>
    Cc: Peter Zijlstra <peterz@infradead.org>
    Cc: Steinar H. Gunderson <sesse@google.com>
    Cc: Thomas Gleixner <tglx@linutronix.de>
    Link: https://lore.kernel.org/r/20250821163820.1132977-2-irogers@google.com
    Signed-off-by: Arnaldo Carvalho de Melo <acme@redhat.com>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 8c32ac03d52773f70f9772b55305c7fb55c8b0a1
Author: Claudiu Beznea <claudiu.beznea.uj@bp.renesas.com>
Date:   Wed Aug 6 12:21:26 2025 +0300

    clk: renesas: r9a08g045: Add MSTOP for GPIO
    
    [ Upstream commit f0cb3463d0244765ab66792a88dc5e2152c130e1 ]
    
    The GPIO module also supports MSTOP. Add it in the description of the gpio
    clock.
    
    Fixes: c49695952746 ("clk: renesas: r9a08g045: Drop power domain instantiation")
    Signed-off-by: Claudiu Beznea <claudiu.beznea.uj@bp.renesas.com>
    Reviewed-by: Geert Uytterhoeven <geert+renesas@glider.be>
    Link: https://lore.kernel.org/20250806092129.621194-2-claudiu.beznea.uj@bp.renesas.com
    Signed-off-by: Geert Uytterhoeven <geert+renesas@glider.be>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit a9b95b7beabb84c786cd264f446c057fe919c45b
Author: Michal Wilczynski <m.wilczynski@samsung.com>
Date:   Sat Aug 16 17:11:10 2025 +0800

    clk: thead: Correct parent for DPU pixel clocks
    
    [ Upstream commit c51a37ffea3813374a8f7955abbba6da25357388 ]
    
    The dpu0_pixelclk and dpu1_pixelclk gates were incorrectly parented to
    the video_pll_clk.
    
    According to the TH1520 TRM, the "dpu0_pixelclk" should be sourced from
    "DPU0 PLL DIV CLK". In this driver, "DPU0 PLL DIV CLK" corresponds to
    the `dpu0_clk` clock, which is a divider whose parent is the
    `dpu0_pll_clk`.
    
    This patch corrects the clock hierarchy by reparenting `dpu0_pixelclk`
    to `dpu0_clk`. By symmetry, `dpu1_pixelclk` is also reparented to its
    correct source, `dpu1_clk`.
    
    Fixes: 50d4b157fa96 ("clk: thead: Add clock support for VO subsystem in T-HEAD TH1520 SoC")
    Reported-by: Icenowy Zheng <uwu@icenowy.me>
    Signed-off-by: Michal Wilczynski <m.wilczynski@samsung.com>
    [Icenowy: add Drew's R-b and rebased atop ccu_gate refactor]
    Reviewed-by: Drew Fustini <fustini@kernel.org>
    Signed-off-by: Icenowy Zheng <uwu@icenowy.me>
    Signed-off-by: Drew Fustini <fustini@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 4ee76291e0842b23d3a67af32b1580a0af4dfe35
Author: Icenowy Zheng <uwu@icenowy.me>
Date:   Sat Aug 16 16:44:45 2025 +0800

    clk: thead: th1520-ap: fix parent of padctrl0 clock
    
    [ Upstream commit 9e99b992c8874f323091d50a5e4727bbd138192d ]
    
    The padctrl0 clock seems to be a child of the perisys_apb4_hclk clock,
    gating the later makes padctrl0 registers stuck too.
    
    Fix this relationship.
    
    Fixes: ae81b69fd2b1 ("clk: thead: Add support for T-Head TH1520 AP_SUBSYS clocks")
    Signed-off-by: Icenowy Zheng <uwu@icenowy.me>
    Reviewed-by: Drew Fustini <fustini@kernel.org>
    Reviewed-by: Troy Mitchell <troy.mitchell@linux.dev>
    Signed-off-by: Drew Fustini <fustini@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit c37f19e63be375d3ea0949c65a943ea7b643c125
Author: Icenowy Zheng <uwu@icenowy.me>
Date:   Sat Aug 16 16:44:44 2025 +0800

    clk: thead: th1520-ap: describe gate clocks with clk_gate
    
    [ Upstream commit aaa75cbd5d4f63e4edf8b74118d367361dcf92f7 ]
    
    Similar to previous situation of mux clocks, the gate clocks of
    clk-th1520-ap drivers are also using a helper that creates a temporary
    struct clk_hw and abandons the struct clk_hw in struct ccu_common, which
    prevents clock gates to be clock parents.
    
    Do the similar refactor of dropping struct ccu_common and directly use
    struct clk_gate here.
    
    This patch mimics the refactor done on struct ccu_mux in 54edba916e29
    ("clk: thead: th1520-ap: Describe mux clocks with clk_mux").
    
    Fixes: ae81b69fd2b1 ("clk: thead: Add support for T-Head TH1520 AP_SUBSYS clocks")
    Signed-off-by: Icenowy Zheng <uwu@icenowy.me>
    Reviewed-by: Drew Fustini <fustini@kernel.org>
    Signed-off-by: Drew Fustini <fustini@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 448daa717973d5938d01e000e7964f5639c87571
Author: Arnd Bergmann <arnd@arndb.de>
Date:   Thu Aug 7 09:22:37 2025 +0200

    clk: npcm: select CONFIG_AUXILIARY_BUS
    
    [ Upstream commit c123519bffd29e6320d3a8c4977f9e5a86d6b83d ]
    
    There are very rare randconfig builds that turn on this driver but
    don't already select CONFIG_AUXILIARY_BUS from another driver, and
    this results in a build failure:
    
    arm-linux-gnueabi-ld: drivers/clk/clk-npcm8xx.o: in function `npcm8xx_clock_driver_init':
    clk-npcm8xx.c:(.init.text+0x18): undefined reference to `__auxiliary_driver_register'
    
    Select the bus here, as all other clk drivers using it do.
    
    Fixes: e0b255df027e ("clk: npcm8xx: add clock controller")
    Signed-off-by: Arnd Bergmann <arnd@arndb.de>
    Link: https://lore.kernel.org/r/20250807072241.4190376-1-arnd@kernel.org
    Signed-off-by: Stephen Boyd <sboyd@kernel.org>
    Signed-off-by: Sasha Levin <sashal@kernel.org>

commit 960b112e34fe681ca4f57a6dd69582c3188067a2
Author: Varad Gautam <varadgautam@google.com>
Date:   Sun Mar 30 16:42:29 2025 +0000

    asm-generic/io.h: Skip trace helpers if rwmmio events are disabled
    
    commit 8327bd4fcb6c1dab01ce5c6ff00b42496836dcd2 upstream.
    
    With `CONFIG_TRACE_MMIO_ACCESS=y`, the `{read,write}{b,w,l,q}{_relaxed}()`
    mmio accessors unconditionally call `log_{post_}{read,write}_mmio()`
    helpers, which in turn call the ftrace ops for `rwmmio` trace events
    
    This adds a performance penalty per mmio accessor call, even when
    `rwmmio` events are disabled at runtime (~80% overhead on local
    measurement).
    
    Guard these with `tracepoint_enabled()`.
    
    Signed-off-by: Varad Gautam <varadgautam@google.com>
    Fixes: 210031971cdd ("asm-generic/io: Add logging support for MMIO accessors")
    Cc: stable@vger.kernel.org
    Signed-off-by: Arnd Bergmann <arnd@arndb.de>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit a553530b3314a0bdc98cf114cdbe204551a70a00
Author: Tomi Valkeinen <tomi.valkeinen@ideasonboard.com>
Date:   Fri Aug 8 11:59:15 2025 +0300

    media: v4l2-subdev: Fix alloc failure check in v4l2_subdev_call_state_try()
    
    commit f37df9a0eb5e43fcfe02cbaef076123dc0d79c7e upstream.
    
    v4l2_subdev_call_state_try() macro allocates a subdev state with
    __v4l2_subdev_state_alloc(), but does not check the returned value. If
    __v4l2_subdev_state_alloc fails, it returns an ERR_PTR, and that would
    cause v4l2_subdev_call_state_try() to crash.
    
    Add proper error handling to v4l2_subdev_call_state_try().
    
    Signed-off-by: Tomi Valkeinen <tomi.valkeinen@ideasonboard.com>
    Fixes: 982c0487185b ("media: subdev: Add v4l2_subdev_call_state_try() macro")
    Reported-by: Dan Carpenter <dan.carpenter@linaro.org>
    Closes: https://lore.kernel.org/all/aJTNtpDUbTz7eyJc%40stanley.mountain/
    Cc: stable@vger.kernel.org
    Reviewed-by: Dan Carpenter <dan.carpenter@linaro.org>
    Signed-off-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Signed-off-by: Hans Verkuil <hverkuil+cisco@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 83fa857f276894c810d109dd31c160cf10238c01
Author: Michael Hennerich <michael.hennerich@analog.com>
Date:   Fri Aug 29 12:25:43 2025 +0100

    iio: frequency: adf4350: Fix ADF4350_REG3_12BIT_CLKDIV_MODE
    
    commit 1d8fdabe19267338f29b58f968499e5b55e6a3b6 upstream.
    
    The clk div bits (2 bits wide) do not start in bit 16 but in bit 15. Fix it
    accordingly.
    
    Fixes: e31166f0fd48 ("iio: frequency: New driver for Analog Devices ADF4350/ADF4351 Wideband Synthesizers")
    Signed-off-by: Michael Hennerich <michael.hennerich@analog.com>
    Signed-off-by: Nuno Sá <nuno.sa@analog.com>
    Link: https://patch.msgid.link/20250829-adf4350-fix-v2-2-0bf543ba797d@analog.com
    Cc: <Stable@vger.kernel.org>
    Signed-off-by: Jonathan Cameron <Jonathan.Cameron@huawei.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 2ed3b2577636a03c6422ddfadb0aca7c798338f2
Author: Sean Christopherson <seanjc@google.com>
Date:   Fri Jul 11 10:27:46 2025 -0700

    KVM: SVM: Emulate PERF_CNTR_GLOBAL_STATUS_SET for PerfMonV2
    
    commit 68e61f6fd65610e73b17882f86fedfd784d99229 upstream.
    
    Emulate PERF_CNTR_GLOBAL_STATUS_SET when PerfMonV2 is enumerated to the
    guest, as the MSR is supposed to exist in all AMD v2 PMUs.
    
    Fixes: 4a2771895ca6 ("KVM: x86/svm/pmu: Add AMD PerfMonV2 support")
    Cc: stable@vger.kernel.org
    Cc: Sandipan Das <sandipan.das@amd.com>
    Link: https://lore.kernel.org/r/20250711172746.1579423-1-seanjc@google.com
    Signed-off-by: Sean Christopherson <seanjc@google.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 1406a670b314f10eedece732ddbe57964b75334a
Author: Hou Wenlong <houwenlong.hwl@antgroup.com>
Date:   Tue Sep 23 08:37:37 2025 -0700

    KVM: x86: Add helper to retrieve current value of user return MSR
    
    commit 9bc366350734246301b090802fc71f9924daad39 upstream.
    
    In the user return MSR support, the cached value is always the hardware
    value of the specific MSR. Therefore, add a helper to retrieve the
    cached value, which can replace the need for RDMSR, for example, to
    allow SEV-ES guests to restore the correct host hardware value without
    using RDMSR.
    
    Cc: stable@vger.kernel.org
    Signed-off-by: Hou Wenlong <houwenlong.hwl@antgroup.com>
    [sean: drop "cache" from the name, make it a one-liner, tag for stable]
    Reviewed-by: Xiaoyao Li <xiaoyao.li@intel.com>
    Link: https://lore.kernel.org/r/20250923153738.1875174-2-seanjc@google.com
    Signed-off-by: Sean Christopherson <seanjc@google.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit d4c322913af71d9cee6889dd8a22873b9fac004b
Author: Olga Kornievskaia <okorniev@redhat.com>
Date:   Tue Aug 19 14:04:02 2025 -0400

    nfsd: unregister with rpcbind when deleting a transport
    
    commit 898374fdd7f06fa4c4a66e8be3135efeae6128d5 upstream.
    
    When a listener is added, a part of creation of transport also registers
    program/port with rpcbind. However, when the listener is removed,
    while transport goes away, rpcbind still has the entry for that
    port/type.
    
    When deleting the transport, unregister with rpcbind when appropriate.
    
    ---v2 created a new xpt_flag XPT_RPCB_UNREG to mark TCP and UDP
    transport and at xprt destroy send rpcbind unregister if flag set.
    
    Suggested-by: Chuck Lever <chuck.lever@oracle.com>
    Fixes: d093c9089260 ("nfsd: fix management of listener transports")
    Cc: stable@vger.kernel.org
    Signed-off-by: Olga Kornievskaia <okorniev@redhat.com>
    Reviewed-by: Jeff Layton <jlayton@kernel.org>
    Signed-off-by: Chuck Lever <chuck.lever@oracle.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 509c344cdfd314b26914b2ccb117e78d7e01eb15
Author: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Date:   Fri Sep 26 12:12:37 2025 +0200

    cpufreq: Make drivers using CPUFREQ_ETERNAL specify transition latency
    
    commit f97aef092e199c10a3da96ae79b571edd5362faa upstream.
    
    Commit a755d0e2d41b ("cpufreq: Honour transition_latency over
    transition_delay_us") caused platforms where cpuinfo.transition_latency
    is CPUFREQ_ETERNAL to get a very large transition latency whereas
    previously it had been capped at 10 ms (and later at 2 ms).
    
    This led to a user-observable regression between 6.6 and 6.12 as
    described by Shawn:
    
    "The dbs sampling_rate was 10000 us on 6.6 and suddently becomes
     6442450 us (4294967295 / 1000 * 1.5) on 6.12 for these platforms
     because the default transition delay was dropped [...].
    
     It slows down dbs governor's reacting to CPU loading change
     dramatically.  Also, as transition_delay_us is used by schedutil
     governor as rate_limit_us, it shows a negative impact on device
     idle power consumption, because the device gets slightly less time
     in the lowest OPP."
    
    Evidently, the expectation of the drivers using CPUFREQ_ETERNAL as
    cpuinfo.transition_latency was that it would be capped by the core,
    but they may as well return a default transition latency value instead
    of CPUFREQ_ETERNAL and the core need not do anything with it.
    
    Accordingly, introduce CPUFREQ_DEFAULT_TRANSITION_LATENCY_NS and make
    all of the drivers in question use it instead of CPUFREQ_ETERNAL.  Also
    update the related Rust binding.
    
    Fixes: a755d0e2d41b ("cpufreq: Honour transition_latency over transition_delay_us")
    Closes: https://lore.kernel.org/linux-pm/20250922125929.453444-1-shawnguo2@yeah.net/
    Reported-by: Shawn Guo <shawnguo@kernel.org>
    Reviewed-by: Mario Limonciello (AMD) <superm1@kernel.org>
    Reviewed-by: Jie Zhan <zhanjie9@hisilicon.com>
    Acked-by: Viresh Kumar <viresh.kumar@linaro.org>
    Cc: 6.6+ <stable@vger.kernel.org> # 6.6+
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Link: https://patch.msgid.link/2264949.irdbgypaU6@rafael.j.wysocki
    [ rjw: Fix typo in new symbol name, drop redundant type cast from Rust binding ]
    Tested-by: Shawn Guo <shawnguo@kernel.org> # with cpufreq-dt driver
    Reviewed-by: Qais Yousef <qyousef@layalina.io>
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit ab826974bc0ba026ecb8a2ed6983a76066c42eca
Author: Petr Tesarik <ptesarik@suse.com>
Date:   Wed Oct 1 08:10:28 2025 +0200

    dma-mapping: fix direction in dma_alloc direction traces
    
    commit 16abbabc004bedeeaa702e11913da9d4fa70e63a upstream.
    
    Set __entry->dir to the actual "dir" parameter of all trace events
    in dma_alloc_class. This struct member was left uninitialized by
    mistake.
    
    Signed-off-by: Petr Tesarik <ptesarik@suse.com>
    Fixes: 3afff779a725 ("dma-mapping: trace dma_alloc/free direction")
    Cc: stable@vger.kernel.org
    Reviewed-by: Sean Anderson <sean.anderson@linux.dev>
    Signed-off-by: Marek Szyprowski <m.szyprowski@samsung.com>
    Link: https://lore.kernel.org/r/20251001061028.412258-1-ptesarik@suse.com
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 02a4679ef96bcd83180ffdde3f7e301f69559724
Author: Brian Norris <briannorris@chromium.org>
Date:   Thu Sep 25 12:42:16 2025 -0700

    PM: runtime: Update kerneldoc return codes
    
    commit fed7eaa4f037361fe4f3d4170649d6849a25998d upstream.
    
    APIs based on __pm_runtime_idle() (pm_runtime_idle(), pm_request_idle())
    do not return 1 when already suspended. They return -EAGAIN. This is
    already covered in the docs, so the entry for "1" is redundant and
    conflicting.
    
    (pm_runtime_put() and pm_runtime_put_sync() were previously incorrect,
    but that's fixed in "PM: runtime: pm_runtime_put{,_sync}() returns 1
    when already suspended", to ensure consistency with APIs like
    pm_runtime_put_autosuspend().)
    
    RPM_GET_PUT APIs based on __pm_runtime_suspend() do return 1 when
    already suspended, but the language is a little unclear -- it's not
    really an "error", so it seems better to list as a clarification before
    the 0/success case. Additionally, they only actually return 1 when the
    refcount makes it to 0; if the usage counter is still non-zero, we
    return 0.
    
    pm_runtime_put(), etc., also don't appear at first like they can ever
    see "-EAGAIN: Runtime PM usage_count non-zero", because in non-racy
    conditions, pm_runtime_put() would drop its reference count, see it's
    non-zero, and return early (in __pm_runtime_idle()). However, it's
    possible to race with another actor that increments the usage_count
    afterward, since rpm_idle() is protected by a separate lock; in such a
    case, we may see -EAGAIN.
    
    Because this case is only seen in the presence of concurrent actors, it
    makes sense to clarify that this is when "usage_count **became**
    non-zero", by way of some racing actor.
    
    Lastly, pm_runtime_put_sync_suspend() duplicated some -EAGAIN language.
    Fix that.
    
    Fixes: 271ff96d6066 ("PM: runtime: Document return values of suspend-related API functions")
    Link: https://lore.kernel.org/linux-pm/aJ5pkEJuixTaybV4@google.com/
    Signed-off-by: Brian Norris <briannorris@chromium.org>
    Reviewed-by: Sakari Ailus <sakari.ailus@linux.intel.com>
    Cc: 6.17+ <stable@vger.kernel.org> # 6.17+
    Signed-off-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit f62934cea32c8f7b11b747975d69bf5afe4264cf
Author: Toke Høiland-Jørgensen <toke@redhat.com>
Date:   Tue Sep 30 13:43:29 2025 +0200

    page_pool: Fix PP_MAGIC_MASK to avoid crashing on some 32-bit arches
    
    commit 95920c2ed02bde551ab654e9749c2ca7bc3100e0 upstream.
    
    Helge reported that the introduction of PP_MAGIC_MASK let to crashes on
    boot on his 32-bit parisc machine. The cause of this is the mask is set
    too wide, so the page_pool_page_is_pp() incurs false positives which
    crashes the machine.
    
    Just disabling the check in page_pool_is_pp() will lead to the page_pool
    code itself malfunctioning; so instead of doing this, this patch changes
    the define for PP_DMA_INDEX_BITS to avoid mistaking arbitrary kernel
    pointers for page_pool-tagged pages.
    
    The fix relies on the kernel pointers that alias with the pp_magic field
    always being above PAGE_OFFSET. With this assumption, we can use the
    lowest bit of the value of PAGE_OFFSET as the upper bound of the
    PP_DMA_INDEX_MASK, which should avoid the false positives.
    
    Because we cannot rely on PAGE_OFFSET always being a compile-time
    constant, nor on it always being >0, we fall back to disabling the
    dma_index storage when there are not enough bits available. This leaves
    us in the situation we were in before the patch in the Fixes tag, but
    only on a subset of architecture configurations. This seems to be the
    best we can do until the transition to page types in complete for
    page_pool pages.
    
    v2:
    - Make sure there's at least 8 bits available and that the PAGE_OFFSET
      bit calculation doesn't wrap
    
    Link: https://lore.kernel.org/all/aMNJMFa5fDalFmtn@p100/
    Fixes: ee62ce7a1d90 ("page_pool: Track DMA-mapped pages and unmap them when destroying the pool")
    Cc: stable@vger.kernel.org # 6.15+
    Tested-by: Helge Deller <deller@gmx.de>
    Signed-off-by: Toke Høiland-Jørgensen <toke@redhat.com>
    Reviewed-by: Mina Almasry <almasrymina@google.com>
    Tested-by: Helge Deller <deller@gmx.de>
    Link: https://patch.msgid.link/20250930114331.675412-1-toke@redhat.com
    Signed-off-by: Jakub Kicinski <kuba@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 9d1a250a7303ad274901aab0e289f6555c549666
Author: Shakeel Butt <shakeel.butt@linux.dev>
Date:   Mon Sep 22 15:02:03 2025 -0700

    memcg: skip cgroup_file_notify if spinning is not allowed
    
    commit fcc0669c5aa681994c507b50f1c706c969d99730 upstream.
    
    Generally memcg charging is allowed from all the contexts including NMI
    where even spinning on spinlock can cause locking issues.  However one
    call chain was missed during the addition of memcg charging from any
    context support.  That is try_charge_memcg() -> memcg_memory_event() ->
    cgroup_file_notify().
    
    The possible function call tree under cgroup_file_notify() can acquire
    many different spin locks in spinning mode.  Some of them are
    cgroup_file_kn_lock, kernfs_notify_lock, pool_workqeue's lock.  So, let's
    just skip cgroup_file_notify() from memcg charging if the context does not
    allow spinning.
    
    Alternative approach was also explored where instead of skipping
    cgroup_file_notify(), we defer the memcg event processing to irq_work [1].
    However it adds complexity and it was decided to keep things simple until
    we need more memcg events with !allow_spinning requirement.
    
    Link: https://lore.kernel.org/all/5qi2llyzf7gklncflo6gxoozljbm4h3tpnuv4u4ej4ztysvi6f@x44v7nz2wdzd/ [1]
    Link: https://lkml.kernel.org/r/20250922220203.261714-1-shakeel.butt@linux.dev
    Fixes: 3ac4638a734a ("memcg: make memcg_rstat_updated nmi safe")
    Signed-off-by: Shakeel Butt <shakeel.butt@linux.dev>
    Acked-by: Michal Hocko <mhocko@suse.com>
    Closes: https://lore.kernel.org/all/20250905061919.439648-1-yepeilin@google.com/
    Cc: Alexei Starovoitov <ast@kernel.org>
    Cc: Johannes Weiner <hannes@cmpxchg.org>
    Cc: Kumar Kartikeya Dwivedi <memxor@gmail.com>
    Cc: Muchun Song <muchun.song@linux.dev>
    Cc: Peilin Ye <yepeilin@google.com>
    Cc: Roman Gushchin <roman.gushchin@linux.dev>
    Cc: Tejun Heo <tj@kernel.org>
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 10d81b1d2d506c6957896f5cfe733884246a3bb1
Author: Zhen Ni <zhen.ni@easystack.cn>
Date:   Thu Aug 14 20:33:24 2025 +0800

    clocksource/drivers/clps711x: Fix resource leaks in error paths
    
    commit cd32e596f02fc981674573402c1138f616df1728 upstream.
    
    The current implementation of clps711x_timer_init() has multiple error
    paths that directly return without releasing the base I/O memory mapped
    via of_iomap(). Fix of_iomap leaks in error paths.
    
    Fixes: 04410efbb6bc ("clocksource/drivers/clps711x: Convert init function to return error")
    Fixes: 2a6a8e2d9004 ("clocksource/drivers/clps711x: Remove board support")
    Signed-off-by: Zhen Ni <zhen.ni@easystack.cn>
    Signed-off-by: Daniel Lezcano <daniel.lezcano@linaro.org>
    Cc: stable@vger.kernel.org
    Link: https://lore.kernel.org/r/20250814123324.1516495-1-zhen.ni@easystack.cn
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 9c80da26fda2fdcaac7f92b5908875b3108830ff
Author: Christian Brauner <brauner@kernel.org>
Date:   Fri Sep 19 17:33:47 2025 +0200

    listmount: don't call path_put() under namespace semaphore
    
    commit c1f86d0ac322c7e77f6f8dbd216c65d39358ffc0 upstream.
    
    Massage listmount() and make sure we don't call path_put() under the
    namespace semaphore. If we put the last reference we're fscked.
    
    Fixes: b4c2bea8ceaa ("add listmount(2) syscall")
    Cc: stable@vger.kernel.org # v6.8+
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 4d50e8360edbef8a94a301fa4d062685e9f64a0b
Author: Christian Brauner <brauner@kernel.org>
Date:   Fri Sep 19 17:03:51 2025 +0200

    statmount: don't call path_put() under namespace semaphore
    
    commit e8c84e2082e69335f66c8ade4895e80ec270d7c4 upstream.
    
    Massage statmount() and make sure we don't call path_put() under the
    namespace semaphore. If we put the last reference we're fscked.
    
    Fixes: 46eae99ef733 ("add statmount(2) syscall")
    Cc: stable@vger.kernel.org # v6.8+
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 159e2db6cb7a7f8684aae929773bc505b5282cbf
Author: Thomas Gleixner <tglx@linutronix.de>
Date:   Wed Aug 13 17:02:30 2025 +0200

    rseq: Protect event mask against membarrier IPI
    
    commit 6eb350a2233100a283f882c023e5ad426d0ed63b upstream.
    
    rseq_need_restart() reads and clears task::rseq_event_mask with preemption
    disabled to guard against the scheduler.
    
    But membarrier() uses an IPI and sets the PREEMPT bit in the event mask
    from the IPI, which leaves that RMW operation unprotected.
    
    Use guard(irq) if CONFIG_MEMBARRIER is enabled to fix that.
    
    Fixes: 2a36ab717e8f ("rseq/membarrier: Add MEMBARRIER_CMD_PRIVATE_EXPEDITED_RSEQ")
    Signed-off-by: Thomas Gleixner <tglx@linutronix.de>
    Reviewed-by: Boqun Feng <boqun.feng@gmail.com>
    Reviewed-by: Mathieu Desnoyers <mathieu.desnoyers@efficios.com>
    Cc: stable@vger.kernel.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 88025faf2aa08c7468d68d8cb31a53b55aae6ee0
Author: Omar Sandoval <osandov@fb.com>
Date:   Fri Sep 19 14:27:51 2025 -0700

    arm64: map [_text, _stext) virtual address range non-executable+read-only
    
    commit 5973a62efa34c80c9a4e5eac1fca6f6209b902af upstream.
    
    Since the referenced fixes commit, the kernel's .text section is only
    mapped starting from _stext; the region [_text, _stext) is omitted. As a
    result, other vmalloc/vmap allocations may use the virtual addresses
    nominally in the range [_text, _stext). This address reuse confuses
    multiple things:
    
    1. crash_prepare_elf64_headers() sets up a segment in /proc/vmcore
       mapping the entire range [_text, _end) to
       [__pa_symbol(_text), __pa_symbol(_end)). Reading an address in
       [_text, _stext) from /proc/vmcore therefore gives the incorrect
       result.
    2. Tools doing symbolization (either by reading /proc/kallsyms or based
       on the vmlinux ELF file) will incorrectly identify vmalloc/vmap
       allocations in [_text, _stext) as kernel symbols.
    
    In practice, both of these issues affect the drgn debugger.
    Specifically, there were cases where the vmap IRQ stacks for some CPUs
    were allocated in [_text, _stext). As a result, drgn could not get the
    stack trace for a crash in an IRQ handler because the core dump
    contained invalid data for the IRQ stack address. The stack addresses
    were also symbolized as being in the _text symbol.
    
    Fix this by bringing back the mapping of [_text, _stext), but now make
    it non-executable and read-only. This prevents other allocations from
    using it while still achieving the original goal of not mapping
    unpredictable data as executable. Other than the changed protection,
    this is effectively a revert of the fixes commit.
    
    Fixes: e2a073dde921 ("arm64: omit [_text, _stext) from permanent kernel mapping")
    Cc: stable@vger.kernel.org
    Signed-off-by: Omar Sandoval <osandov@fb.com>
    Signed-off-by: Will Deacon <will@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit e7a2664e9d54a7393e930abbea21b6d4d542507f
Author: Qu Wenruo <wqu@suse.com>
Date:   Fri Sep 19 14:33:23 2025 +0930

    btrfs: fix the incorrect max_bytes value for find_lock_delalloc_range()
    
    commit 7b26da407420e5054e3f06c5d13271697add9423 upstream.
    
    [BUG]
    With my local branch to enable bs > ps support for btrfs, sometimes I
    hit the following ASSERT() inside submit_one_sector():
    
            ASSERT(block_start != EXTENT_MAP_HOLE);
    
    Please note that it's not yet possible to hit this ASSERT() in the wild
    yet, as it requires btrfs bs > ps support, which is not even in the
    development branch.
    
    But on the other hand, there is also a very low chance to hit above
    ASSERT() with bs < ps cases, so this is an existing bug affect not only
    the incoming bs > ps support but also the existing bs < ps support.
    
    [CAUSE]
    Firstly that ASSERT() means we're trying to submit a dirty block but
    without a real extent map nor ordered extent map backing it.
    
    Furthermore with extra debugging, the folio triggering such ASSERT() is
    always larger than the fs block size in my bs > ps case.
    (8K block size, 4K page size)
    
    After some more debugging, the ASSERT() is trigger by the following
    sequence:
    
     extent_writepage()
     |  We got a 32K folio (4 fs blocks) at file offset 0, and the fs block
     |  size is 8K, page size is 4K.
     |  And there is another 8K folio at file offset 32K, which is also
     |  dirty.
     |  So the filemap layout looks like the following:
     |
     |  "||" is the filio boundary in the filemap.
     |  "//| is the dirty range.
     |
     |  0        8K       16K        24K         32K       40K
     |  |////////|        |//////////////////////||////////|
     |
     |- writepage_delalloc()
     |  |- find_lock_delalloc_range() for [0, 8K)
     |  |  Now range [0, 8K) is properly locked.
     |  |
     |  |- find_lock_delalloc_range() for [16K, 40K)
     |  |  |- btrfs_find_delalloc_range() returned range [16K, 40K)
     |  |  |- lock_delalloc_folios() locked folio 0 successfully
     |  |  |
     |  |  |  The filemap range [32K, 40K) got dropped from filemap.
     |  |  |
     |  |  |- lock_delalloc_folios() failed with -EAGAIN on folio 32K
     |  |  |  As the folio at 32K is dropped.
     |  |  |
     |  |  |- loops = 1;
     |  |  |- max_bytes = PAGE_SIZE;
     |  |  |- goto again;
     |  |  |  This will re-do the lookup for dirty delalloc ranges.
     |  |  |
     |  |  |- btrfs_find_delalloc_range() called with @max_bytes == 4K
     |  |  |  This is smaller than block size, so
     |  |  |  btrfs_find_delalloc_range() is unable to return any range.
     |  |  \- return false;
     |  |
     |  \- Now only range [0, 8K) has an OE for it, but for dirty range
     |     [16K, 32K) it's dirty without an OE.
     |     This breaks the assumption that writepage_delalloc() will find
     |     and lock all dirty ranges inside the folio.
     |
     |- extent_writepage_io()
        |- submit_one_sector() for [0, 8K)
        |  Succeeded
        |
        |- submit_one_sector() for [16K, 24K)
           Triggering the ASSERT(), as there is no OE, and the original
           extent map is a hole.
    
    Please note that, this also exposed the same problem for bs < ps
    support. E.g. with 64K page size and 4K block size.
    
    If we failed to lock a folio, and falls back into the "loops = 1;"
    branch, we will re-do the search using 64K as max_bytes.
    Which may fail again to lock the next folio, and exit early without
    handling all dirty blocks inside the folio.
    
    [FIX]
    Instead of using the fixed size PAGE_SIZE as @max_bytes, use
    @sectorsize, so that we are ensured to find and lock any remaining
    blocks inside the folio.
    
    And since we're here, add an extra ASSERT() to
    before calling btrfs_find_delalloc_range() to make sure the @max_bytes is
    at least no smaller than a block to avoid false negative.
    
    Cc: stable@vger.kernel.org # 5.15+
    Signed-off-by: Qu Wenruo <wqu@suse.com>
    Signed-off-by: David Sterba <dsterba@suse.com>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit b8f70f9479baa24b06201fbd9bc51c18897496bc
Author: Aleksa Sarai <cyphar@cyphar.com>
Date:   Thu Aug 7 03:55:23 2025 +1000

    fscontext: do not consume log entries when returning -EMSGSIZE
    
    commit 72d271a7baa7062cb27e774ac37c5459c6d20e22 upstream.
    
    Userspace generally expects APIs that return -EMSGSIZE to allow for them
    to adjust their buffer size and retry the operation. However, the
    fscontext log would previously clear the message even in the -EMSGSIZE
    case.
    
    Given that it is very cheap for us to check whether the buffer is too
    small before we remove the message from the ring buffer, let's just do
    that instead. While we're at it, refactor some fscontext_read() into a
    separate helper to make the ring buffer logic a bit easier to read.
    
    Fixes: 007ec26cdc9f ("vfs: Implement logging through fs_context")
    Cc: David Howells <dhowells@redhat.com>
    Cc: stable@vger.kernel.org # v5.2+
    Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>
    Link: https://lore.kernel.org/20250807-fscontext-log-cleanups-v3-1-8d91d6242dc3@cyphar.com
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

commit 34451f435c99988c2b02ab24c591db4a0315c495
Author: Thomas Weißschuh <thomas.weissschuh@linutronix.de>
Date:   Tue Aug 5 14:38:08 2025 +0200

    fs: always return zero on success from replace_fd()
    
    commit 708c04a5c2b78e22f56e2350de41feba74dfccd9 upstream.
    
    replace_fd() returns the number of the new file descriptor through the
    return value of do_dup2(). However its callers never care about the
    specific returned number. In fact the caller in receive_fd_replace() treats
    any non-zero return value as an error and therefore never calls
    __receive_sock() for most file descriptors, which is a bug.
    
    To fix the bug in receive_fd_replace() and to avoid the same issue
    happening in future callers, signal success through a plain zero.
    
    Suggested-by: Al Viro <viro@zeniv.linux.org.uk>
    Link: https://lore.kernel.org/lkml/20250801220215.GS222315@ZenIV/
    Fixes: 173817151b15 ("fs: Expand __receive_fd() to accept existing fd")
    Fixes: 42eb0d54c08a ("fs: split receive_fd_replace from __receive_fd")
    Cc: stable@vger.kernel.org
    Signed-off-by: Thomas Weißschuh <thomas.weissschuh@linutronix.de>
    Link: https://lore.kernel.org/20250805-fix-receive_fd_replace-v3-1-b72ba8b34bac@linutronix.de
    Signed-off-by: Christian Brauner <brauner@kernel.org>
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>


--------------------