"use client"
import React, { ChangeEvent, useState } from 'react';
import Image from 'next/image';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';

interface PredictionData {
  image_path: string;
  entities: string[];
}

interface InputFileProps {}

const Card = ({ data }: { data: PredictionData }) => (
  <div className="max-w-sm rounded overflow-hidden shadow-lg">
    <div className="px-6 py-4">
      <div className="font-bold text-xl mb-2">Entities: {data.entities}</div>
      {/* <p className="text-gray-700 text-base">Predicted Entities: {data.predictions.join(', ')}</p> */}
    </div>
  </div>
);

export default function InputFile(props: InputFileProps) {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [predictionData, setPredictionData] = useState<PredictionData | null>(null);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];

    if (file) {
      setSelectedFile(file);
    }
  };

  const handleSubmit = async () => {
    if (!selectedFile) return;

    try {
      const formData = new FormData();
      formData.append('image', selectedFile);

      const response = await fetch('http://localhost:8000/ner-prescription', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        console.log(data)
        setPredictionData(data);
      } else {
        throw new Error('Failed to upload image');
      }
    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };

  return (
    <div className="grid w-full max-w-sm items-center gap-1.5">
      <Label htmlFor="picture">Dental Prescription</Label>
      <Input id="picture" type="file" onChange={handleFileChange} />
      {selectedFile && (
        <div className="mt-2">
          <Image src={URL.createObjectURL(selectedFile)} alt="Preview" width={500} height={500} />
        </div>
      )}
      <button
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        onClick={handleSubmit}
      >
        Upload Image
      </button>
      {/* console.log(predictionData) */}
      {predictionData && (
        <div className="mt-4">
          <Card data={predictionData} />
        </div>
      )}
    </div>
  );
}
