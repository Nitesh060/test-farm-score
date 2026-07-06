export interface Farmer {
  id: number;
  name: string;
  phone: string;
}

export interface Farm {
  id: number;
  farmer_id: number;
  area_hectares: number;
  location_name: string;
}
