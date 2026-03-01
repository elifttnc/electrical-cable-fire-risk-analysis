================================================================
%  ELEKTRIK KABLOLARINDA YANGIN RISKI ANALIZI
%  MATLAB Sinyal Isleme ve Dogrulama Kodlari
%
%  Bu kod ile:
%  1) Akim sinyalinin THD analizi yapilir
%  2) Sicaklik ve risk birlikte degerlendirilir
%  3) Zaman-frekans spektrogrami cikarilir
% ================================================================

clc;
clear;
close all;

%% ----------------------------------------------------------------
%  VERI OKUMA
%  Python simulasyonundan uretilen CSV dosyasi MATLAB ortamina aktarilir
% ----------------------------------------------------------------

data = readtable('proje_verileri.csv');

fs = 2000;                 % Ornekleme frekansi (Hz)
akim = data.Akim;          % Akim verisi
sicaklik = data.Sicaklik;  % Sicaklik verisi
risk = data.Risk;          % Risk skoru
zaman = data.Zaman;        % Zaman ekseni


%% ----------------------------------------------------------------
%  1) HARMONIK ANALIZI (THD)
%  Akim sinyalinin frekans bilesenleri ve harmonik bozulma incelenir
% ----------------------------------------------------------------

figure('Name','THD Analizi','Color','w');

thd(akim, fs);

title('Akim Sinyali Toplam Harmonik Distorsiyon (THD) Analizi');
xlabel('Frekans (Hz)');
ylabel('Genlik (dB)');
grid on;


%% ----------------------------------------------------------------
%  2) TERMAL GELISIM VE RISK KARSILASTIRMASI
%  Sicaklik artisi ile algoritmanin risk ciktisi birlikte gosterilir
% ----------------------------------------------------------------

figure('Name','Termal ve Risk Analizi','Color','w');

yyaxis left
plot(zaman, sicaklik, 'b-', 'LineWidth', 2);
ylabel('Kablo Sıcakligi (°C)');
hold on;

% Kritik sicaklik siniri (PVC izolasyon için ~80°C)
yline(80, 'r--', 'Kritik Eşik (80°C)', ...
      'LabelVerticalAlignment', 'bottom');

yyaxis right
plot(zaman, risk, 'r-', 'LineWidth', 2);
ylabel('Yangin Risk Skoru (0-1)');
ylim([0 1.1]);

xlabel('Zaman (s)');
title('Sıcaklık Artisi ve Algoritma Risk Ciktisinin Karsilastirilmasi');
legend('Sicaklik','Kritik Sinir','Risk Skoru','Location','northwest');
grid on;


%% ----------------------------------------------------------------
%  3) SPEKTROGRAM (ZAMAN-FREKANS ANALIZI)
%  Harmoniklerin zamanla degisimi renk haritasi ile gosterilir
% ----------------------------------------------------------------

figure('Name','Spektrogram','Color','w');

spectrogram(akim, 100, 80, 100, fs, 'yaxis');
title('Akım Sinyali Zaman-Frekans Spektrogramı');
xlabel('Zaman (s)');
ylabel('Frekans (kHz)');
colorbar;
