/*
  Warnings:

  - You are about to drop the column `tire` on the `clans` table. All the data in the column will be lost.
  - Added the required column `tier` to the `clans` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "clans" DROP COLUMN "tire",
ADD COLUMN     "tier" INTEGER NOT NULL;
