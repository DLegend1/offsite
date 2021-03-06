﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;

namespace SIMP
{
    public partial class Form1 : Form
    {
        public int time = 0;
        public int timer = 0;
        public Form1()
        {
            InitializeComponent();
            cbox_seconds.SelectedIndex = 0;
            cbox_minutes.SelectedIndex = 0;
            cbox_hours.SelectedIndex = 0;
            cbox_days.SelectedIndex = 0;
            rbtn_lockscreen.Checked = true;
        }


        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }
        private void rbtn_shutdown_CheckedChanged(object sender, EventArgs e)
        {
        }
        private void rbtn_restart_CheckedChanged(object sender, EventArgs e)
        {
        }
        private void rbtn_lockscreen_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void btn_failsafe_Click(object sender, EventArgs e)
        {
        System.Diagnostics.Process.Start("Shutdown", "-a");
        }

        private void btn_start_Click(object sender, EventArgs e)
        {
            timer = cbox_seconds.SelectedIndex * 5 + cbox_minutes.SelectedIndex * 5 *60 + cbox_hours.SelectedIndex *3600 + cbox_days.SelectedIndex * 86400;
            t_timeleft.Start();
        }

        private void cbox_seconds_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void cbox_minutes_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void cbox_hours_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void cbox_days_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void t_timeleft_Tick(object sender, EventArgs e)
        {
            timer--;
            int days    =   timer / 86400;
            int hours   =   (timer - days * 86400) / 3600;
            int minutes =   (timer - days * 86400 - hours * 3600) / 60;
            int seconds =   (timer - days * 86400 - hours * 3600 - minutes * 60);
            if (days <= 10)
            {
                lbl_time.Text = "0" + Convert.ToString(days) + ":";
            }
            else {
                lbl_time.Text = Convert.ToString(days) + ":";
            }
            if (hours <= 10)
            {
                lbl_time.Text = lbl_time.Text + "0" + Convert.ToString(hours) + ":";
            }
            else
            {
                lbl_time.Text = lbl_time.Text + Convert.ToString(hours) + ":";
            }
            if (minutes <= 10)
            {
                lbl_time.Text = lbl_time.Text + "0" + Convert.ToString(minutes) + ":";
            }
            else
            {
                lbl_time.Text = lbl_time.Text + Convert.ToString(minutes) + ":";
            }
            if (seconds <= 10)
            {
                lbl_time.Text = lbl_time.Text + "0" + Convert.ToString(seconds);
            }
            else
            {
                lbl_time.Text = lbl_time.Text + Convert.ToString(seconds);
            }
            if (timer <= 0)
            {
                if (rbtn_shutdown.Checked.Equals(true))
                {
                    System.Diagnostics.Process.Start("Shutdown", "-s");
                };
                if (rbtn_restart.Checked.Equals(true))
                { 
                    System.Diagnostics.Process.Start("Shutdown", "-r");
                };
                if (rbtn_lockscreen.Checked.Equals(true))
                {
                    System.Diagnostics.Process.Start("Rundll32", "User32.dll,LockWorkStation");
                }
                time = 0;
                t_timeleft.Stop();
            }
        }

        private void btn_stop_Click(object sender, EventArgs e)
        {
            time = 0;
            t_timeleft.Stop();
        }

        private void lbl_time_Click(object sender, EventArgs e)
        {

        }
    }
}
        // Shutdown and restart
        //Show Timer
        //int num = Convert.ToInt32(textBox1.Text);
        //textBox1.Text = Convert.ToString(num + 1);

        //Stop shutdown or restart
        //timer1.Start();