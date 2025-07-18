using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace EMC_Design
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void groupBox2_Enter(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void label23_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            string dosyaYolu = "C:\\Users\\xxtra\\OneDrive\\Desktop\\kodlar\\lab\\EMC_Design\\EMC_Design\\bin\\Debug\\emc.txt";
            try
            {
                // Dosyayı oku
                string metin = File.ReadAllText(dosyaYolu);

                // Virgüllerden sayıları ayır
                string[] sayiDizisi = metin.Split(',');


                sayiDizisi[0] = textBox1.Text;
                sayiDizisi[1] = textBox2.Text;
                sayiDizisi[2] = textBox3.Text;
                sayiDizisi[3] = textBox4.Text;
                sayiDizisi[4] = textBox5.Text;
                sayiDizisi[5] = textBox6.Text;

                // Sayıları tekrar virgülle birleştir
                string yeniMetin = string.Join(",", sayiDizisi);

                // Dosyayı güncelle
                File.WriteAllText(dosyaYolu, yeniMetin);

                Console.WriteLine("Dosya güncellendi.");




                // Konsol komutunu belirtin
                string command = "python C:\\Users\\xxtra\\OneDrive\\Desktop\\kodlar\\lab\\EMC_Design\\EMC_Design\\bin\\Debug\\emc.py";
                

                // Komutu çalıştır
                Process.Start("cmd.exe", "/c " + command);

                Thread.Sleep(2000);
                // Dosyayı oku
                string aaa = File.ReadAllText(dosyaYolu);

                // Virgüllerden sayıları ayır
                string[] bbbb = aaa.Split(',');

                label19.Text = bbbb[6];
                label17.Text = bbbb[7];
                label16.Text = bbbb[8];
                label18.Text = bbbb[9];
                label15.Text = bbbb[10];
                


            }
            catch (Exception ex)
            {
                Console.WriteLine("Hata: " + ex.Message);
            }
        }

        private void label25_Click(object sender, EventArgs e)
        {
            
        }

        private void groupBox1_Enter_1(object sender, EventArgs e)
        {

        }
    }
}
