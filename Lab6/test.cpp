// ImgOpt.cpp : ���ļ����� "main" ����������ִ�н��ڴ˴���ʼ��������
//
#include <iostream>
#include <Windows.h>
#include <malloc.h>
#include <vector>

using namespace std;

string imgPath = "C:\\lab6\\Moment.bmp";
string saveImgPath = "C:\\lab6\\test.bmp";

//�Զ�����һ��ImgInfo�Ľṹ�壬����BMP�ļ�ͷ��BMP��Ϣͷ�����ص��RGBֵ��
//Ŀǰֻ֧��24λͼ��Ķ�ȡ����ʾ

typedef struct{
    BITMAPFILEHEADER bf;
    BITMAPINFOHEADER bi;
    vector<vector<char>> imgData;
}ImgInfo;

//����ͼƬ·����ȡBmpͼ������ImgInfo����
ImgInfo readBitmap(string imgPath) {
    ImgInfo imgInfo;
    char* buf;                                              //�����ļ���ȡ������
    char* p;

    FILE* fp;
    fopen_s(&fp, imgPath.c_str(), "rb");
    if (fp == NULL) {
        cout << "���ļ�ʧ��!" << endl;
        exit(0);
    }

    fread(&imgInfo.bf, sizeof(BITMAPFILEHEADER), 1, fp);
    fread(&imgInfo.bi, sizeof(BITMAPINFOHEADER), 1, fp);

    // cout << imgInfo.bi.biBitCount;
    cout << "bfType " << imgInfo.bf.bfType << endl;
    cout << "bfSize " << imgInfo.bf.bfSize << endl;
    cout << "bfReserved1 " << imgInfo.bf.bfReserved1 << endl;
    cout << "bfReserved2 " << imgInfo.bf.bfReserved2 << endl;
    cout << "bfOffBits " << imgInfo.bf.bfOffBits << endl;

    cout << "biWidth " << imgInfo.bi.biWidth << endl;
    cout << "biHeight " << imgInfo.bi.biHeight << endl;
    cout << "biBitCount " << imgInfo.bi.biBitCount << endl;
    cout << "biClrImportant " << imgInfo.bi.biClrImportant << endl;
    cout << "biClrUsed " << imgInfo.bi.biClrUsed << endl;
    cout << "biCompression " << imgInfo.bi.biCompression << endl;
    cout << "biPlanes " << imgInfo.bi.biPlanes << endl;
    cout << "biSize " << imgInfo.bi.biSize << endl;
    cout << "biXPelsPerMeter " << imgInfo.bi.biXPelsPerMeter << endl;
    cout << "biYPelsPerMeter " << imgInfo.bi.biYPelsPerMeter << endl;

    if (imgInfo.bi.biBitCount != 24){
        cout << "��֧�ָø�ʽ��BMPλͼ��" << endl;
        exit(0);
    }

    fseek(fp, imgInfo.bf.bfOffBits, 0);

    buf = (char*)malloc(imgInfo.bi.biWidth * imgInfo.bi.biHeight * 3);
    fread(buf, 1, imgInfo.bi.biWidth * imgInfo.bi.biHeight * 3, fp);

    p = buf;

    vector<vector<char>> imgData;
    for (int y = 0; y < imgInfo.bi.biHeight; y++){
        for (int x = 0; x < imgInfo.bi.biWidth; x++) {
            vector<char> vRGB;

            vRGB.push_back(*(p++));     //blue
            vRGB.push_back(*(p++));     //green
            vRGB.push_back(*(p++));     //red

            if (x == imgInfo.bi.biWidth - 1)
            {
                for (int k = 0; k < imgInfo.bi.biWidth % 4; k++) p++;
            }
            imgData.push_back(vRGB);
        }
    }
    fclose(fp);
    imgInfo.imgData = imgData;
    return imgInfo;
}

void showBitmap(ImgInfo imgInfo) {
    HWND hWindow;                                                //���ھ��
    HDC hDc;                                                     //��ͼ�豸�������
    int yOffset = 150;
    hWindow = GetForegroundWindow();
    hDc = GetDC(hWindow);

    int posX, posY;
    for (int i = 0; i < imgInfo.imgData.size(); i++){
        char blue = imgInfo.imgData.at(i).at(0);
        char green = imgInfo.imgData.at(i).at(1);
        char red = imgInfo.imgData.at(i).at(2);

        posX = i % imgInfo.bi.biWidth;
        posY = imgInfo.bi.biHeight - i / imgInfo.bi.biWidth + yOffset;
        SetPixel(hDc, posX, posY, RGB(red, green, blue));
    }
}

void saveBitmap(ImgInfo imgInfo) {
    FILE* fpw;
    fopen_s(&fpw, saveImgPath.c_str(), "wb");
    fwrite(&imgInfo.bf, sizeof(BITMAPFILEHEADER), 1, fpw);  //д���ļ�ͷ
    fwrite(&imgInfo.bi, sizeof(BITMAPINFOHEADER), 1, fpw);  //д���ļ�ͷ��Ϣ

    int size = imgInfo.bi.biWidth * imgInfo.bi.biHeight;
    for (int i = 0; i < size; i++) {
        fwrite(&imgInfo.imgData.at(i).at(0), 1, 1, fpw);
        fwrite(&imgInfo.imgData.at(i).at(1), 1, 1, fpw);
        fwrite(&imgInfo.imgData.at(i).at(2), 1, 1, fpw);

        if (i % imgInfo.bi.biWidth == imgInfo.bi.biWidth - 1) {
            char ch = '0';
            for (int j = 0; j < imgInfo.bi.biWidth % 4; j++) {
                fwrite(&ch, 1, 1, fpw);
            }
        }
    }
    fclose(fpw);
    cout << "�ѱ���ͼ����: " + saveImgPath << endl;
}

int main() {
    ImgInfo imgInfo = readBitmap(imgPath);
    //showBitmap(imgInfo);
    saveBitmap(imgInfo);
}
