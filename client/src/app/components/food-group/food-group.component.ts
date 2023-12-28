import { Component, ElementRef, OnInit, Signal, ViewChild, inject } from '@angular/core';
import { FoodGroupService } from '../../services/food-group/food-group.service';
import { FoodGroup } from '../../models/food-group.model';
import { take } from 'rxjs';
import { FormsModule } from '@angular/forms';
import { FoodGroupRequest } from '../../models/food-group-request.model';

@Component({
  selector: 'app-food-group',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './food-group.component.html',
  styleUrl: './food-group.component.scss'
})
export class FoodGroupComponent implements OnInit {
  foodGroupService = inject(FoodGroupService);

  @ViewChild('closeEditFoodGroupModalButton') closeEditFoodGroupModalButton?: ElementRef;

  foodGroups: Signal<FoodGroup[]> = this.foodGroupService.foodGroups.asReadonly();
  // foodGroups: FoodGroup[] = [];
  foodGroupName = '';
  foodGroupEdit?: FoodGroup;

  ngOnInit(): void {
    // this.getFoodGroups();
  }

  addFoodGroup(name: string): void {
    const foodGroupRequest: FoodGroupRequest = {
      name: name
    };
    this.foodGroupService.addFoodGroup(foodGroupRequest).pipe(take(1)).subscribe({
      next: (foodGroup) => {
        // this.foodGroupService.pushFoodGroup(foodGroup);
        this.foodGroups().push(foodGroup);
      }
    });
  }

  deleteFoodGroup(id: number, index: number): void {
    this.foodGroupService.deleteFoodGroup(id).pipe(take(1)).subscribe({
      next: () => {
        this.foodGroups().splice(index, 1);
        // this.foodGroupService.spliceFoodGroup(index);
      }
    });
  }

  editFoodGroup(foodGroup: FoodGroup): void {
    this.foodGroupEdit = Object.assign({}, foodGroup);
  }

  // getFoodGroups(): void {
  //   this.foodGroupService.getFoodGroups().pipe(take(1)).subscribe({
  //     next: (foodGroups) => {
  //       this.foodGroups = foodGroups;
  //     }
  //   });
  // }

  updateFoodGroup(foodGroupUpdate: FoodGroup): void {
    const foodGroupRequest: FoodGroupRequest = {
      id: foodGroupUpdate.id,
      name: foodGroupUpdate.name
    };
    this.foodGroupService.updateFoodGroup(foodGroupRequest).pipe(take(1)).subscribe({
      next: (updatedFoodGroup) => {
        let foodGroupToUpdate = this.foodGroups().find((foodGroup: FoodGroup) => {
          return foodGroup.id === updatedFoodGroup.id;
        });
        if (foodGroupToUpdate) {
          Object.assign(foodGroupToUpdate, updatedFoodGroup);
          this.closeEditFoodGroupModalButton?.nativeElement.click();
        }
      }
    });
  }


}
